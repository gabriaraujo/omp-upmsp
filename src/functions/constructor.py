from config import *
from heapq import *


def set_routes(file: Data,
               wl: List[float],
               inp: List[float],
               time: List[float]) -> List[List[int]]:
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


def set_engines(file: Data, routes: List[Route]) -> List[List[int]]:
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
