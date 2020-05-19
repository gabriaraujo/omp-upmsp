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
        visited = [False] * len(file['stockpiles'])
        route, pos = [], eng.pos_ini

        while not all(visited):
            try:
                # encontra a pilha com menor tempo de acesso
                faster, pos = min((time_travel + start_time[eng.id - 1], i) 
                                  for i, (time_travel, is_visited) 
                                  in enumerate(zip(travel[pos], visited))
                                  if wl[i] > 0 and is_visited is False)
    
                # calcula o tempo que a máquina permaneceu operando na pilha
                duration = round(wl[pos] / eng.speed_reclaim, 1)
                
                # caso a máquina também precise reabastecer a pilha visitada
                if inp[pos] > 0:
                    reset = travel[pos][pos]
                    duration += round(inp[pos] / eng.speed_stack, 1) + reset

                # adiciona o tempo de operação ao tempo inicial de cada trabalho
                start_time[eng.id - 1] += duration + faster

                # adiciona os dados à lista de rotas da máquina em questão
                route.append((faster, eng.id, pos))
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
    visited = [False] * len(file['stockpiles'])

    while routes:
        route = heappop(routes)
        
        # route[0] é o tempo gasto para acessar a pilha, utilizado pela heap
        # route[1] é o id da máquina, que será seu índice na lista 
        # route[2] é a posição da pilha que entrará na rota da máquina

        eng, stp = route[1] - 1, route[2]
        if not visited[stp]:
            result[eng].append(stp)
            visited[stp] = True

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
        i = file['engines'].index(eng)

        for j, stp in enumerate(route):
            # tempo de configuração caso haja mais de uma tarefa na mesma pilha
            reset = 0.0

            # tempo da recuperação, de viagem e configuração até a pilha
            duration = round(wl[stp] / eng.speed_reclaim, 1)
            time_travel = travel[stp][route[j - 1]] \
                if stp is not eng.pos_ini else travel[stp][stp]

            # realiza a atividade de empilhamento antes de realizar a retirada
            if inp[stp] > 0:
                stacks.append({
                    'weight': round(inp[stp], 1),
                    'stockpile': stp + 1,
                    'engine': eng.id,
                    'start_time': round(time[i] + time_travel, 1),
                    'duration': round(inp[stp] / eng.speed_stack, 1),
                })

                # adiciona o tempo de empilhamento caso haja alguma entrada
                time[i] += stacks[-1]['duration']
                reset += travel[stp][stp]
                inp[stp] = 0.0

            # atividade de retirada de minério da pilha
            reclaims.append({
                'weight': round(wl[stp], 1),
                'stockpile': stp + 1,
                'engine': eng.id,
                'start_time': round(time[i] + time_travel + reset, 1),
                'duration': duration,
                'output': id
            }) if wl[stp] > 0 else None

            time[i] += duration + time_travel

        # altera a posição inicial da máquina para sua última pilha visitada
        try:
            eng.pos_ini = route[-1]

        # caso a máquina não tenha recebido nenhuma tarefa
        except IndexError:
            pass

    return stacks, reclaims