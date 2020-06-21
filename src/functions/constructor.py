from config import *
from heapq import *


def set_routes(file: Data,
               wl: List[float],
               inp: List[float],
               time: List[float]) -> Routes:
    """define a ordem de funcionamento das máquinas."""

    routes = []
    travel = file['time_travel']
    start_time = time.copy()

    for eng in file['engines']:
        # lista para indicar se a máquina já visitou a pilha
        visited = [False for stp in file['stockpiles']
                   if eng.rail in stp.rails]

        # lista com as rotas da máquina e variável com sua posição inicial
        route, pos = [], eng.pos_ini

        while not all(visited):
            try:
                # encontra a pilha com menor tempo de acesso
                faster, pos = min((time_travel + start_time[eng.id - 1], i)
                                  for i, (time_travel, is_visited)
                                  in enumerate(zip(travel[pos], visited))
                                  if wl[i] > 0 and is_visited is False
                                  and eng.rail in file['stockpiles'][i].rails)

                # indica qual atividade será realizada pela máquina
                # r para retomar, s para empilhar e b para ambas
                atv = 'r'

                # calcula o tempo que a máquina permaneceu operando na pilha
                duration = round(wl[pos] / eng.speed_reclaim, 1) \
                    if eng.speed_reclaim > 0 else 0

                # caso a máquina precise reabastecer a pilha visitada
                if inp[pos] > 0:
                    reset = travel[pos][pos] if eng.speed_reclaim > 0 else 0
                    duration += round(inp[pos] / eng.speed_stack, 1) + reset \
                        if eng.speed_stack > 0 else 0

                    atv = 's' if eng.speed_stack > 0 else atv
                    atv = 'b' if eng.speed_reclaim > 0 and \
                        eng.speed_stack > 0 else atv

                if duration > 0:
                    # adiciona o tempo de operação ao tempo inicial do trabalho
                    start_time[eng.id - 1] += duration + faster

                    # adiciona os dados à lista de rotas da máquina em questão
                    route.append((faster, eng.id, pos, atv))

                visited[pos] = True

            # caso o modelo seja inviável, a função min() lança uma exceção
            except ValueError:
                break

        # anexa a rota da máquina à lista de rotas
        routes.append(route)

    return set_engines(file, routes)


def set_engines(file: Data, routes: List[Route]) -> Routes:
    """define onde cada máquina irá atuar baseado em suas rotas."""

    routes = [item for sublist in routes for item in sublist]
    heapify(routes)

    # result salva as lista de pilhas visitadas por cada máquina
    result = [[] for _ in range(len(file['engines']))]
    work = [''] * len(file['stockpiles'])

    while routes:
        route = heappop(routes)

        # route[0] é o tempo gasto para acessar a pilha, utilizado pela heap
        # route[1] é o id da máquina, que será seu índice na lista 
        # route[2] é a posição da pilha que entrará na rota da máquina
        # route[3] é o tipo de atividade que será realizada na pilha

        eng, stp, atv = route[1] - 1, route[2], route[3]
        if work[stp] is not atv and work[stp] is not 'b':
            if atv is 'b' and work[stp] is 's':
                result[eng].append((stp, 'r'))
                work[stp] = 'b'

            elif atv is 'b' and work[stp] is 'r':
                result[eng].append((stp, 's'))
                work[stp] = 'b'

            else:
                result[eng].append((stp, atv))
                work[stp] = atv

    return result


def set_works(file: Data,
              id: int,
              wl: List[float],
              inp: List[float],
              time: List[float],
              routes: Routes) -> Tuple[Works, Works]:
    """define as operações realizadas em cada pilha, a velocidade e o tempo."""

    stacks, reclaims = [], []
    travel = file['time_travel']

    for eng, route, in zip(file['engines'], routes):
        for j, (stp, atv) in enumerate(route):
            # tempo de configuração caso haja mais de uma tarefa na mesma pilha
            reset = 0.0

            # tempo da recuperação, de viagem e configuração até a pilha
            duration = round(wl[stp] / eng.speed_reclaim, 1) \
                if eng.speed_reclaim > 0 else 0

            time_travel = travel[stp][route[j - 1][0]] \
                if stp is not eng.pos_ini else travel[stp][stp]

            # realiza a atividade de empilhamento antes de realizar a retirada
            if atv is 's' or atv is 'b':
                stacks.append({
                    'weight': round(inp[stp], 1),
                    'stockpile': stp + 1,
                    'engine': eng.id,
                    'start_time': round(time[eng.id - 1] + time_travel, 1),
                    'duration': round(inp[stp] / eng.speed_stack, 1),
                })

                # adiciona o tempo de empilhamento caso haja alguma entrada
                time[eng.id - 1] += stacks[-1]['duration']
                reset += travel[stp][stp]
                inp[stp] = 0.0

            # atividade de retirada de minério da pilha
            reclaims.append({
                'weight': round(wl[stp], 1),
                'stockpile': stp + 1,
                'engine': eng.id,
                'start_time': round(time[eng.id - 1] + time_travel + reset, 1),
                'duration': duration,
                'output': id
            }) if atv is 'r' or atv is 'b' else None

            time[eng.id - 1] += duration + time_travel

        # altera a posição inicial da máquina para sua última pilha visitada
        try:
            eng.pos_ini = route[-1][0]

        # caso a máquina não tenha recebido nenhuma tarefa
        except IndexError:
            pass

    return stacks, reclaims
