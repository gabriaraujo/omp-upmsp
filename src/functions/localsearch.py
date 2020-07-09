from functions import set_works
from config import *
import random
import math


def local_search(file: Data,
                 id: int,
                 wl: List[float],
                 inp: List[float],
                 time: List[float],
                 routes: Routes) -> Tuple[Works, Works]:
    """realiza a busca local nas rotas geradas pelo construtor."""

    # salva o tempo e input inicial para poder calcular a rota corretamente
    initial_time = time.copy()
    initial_inp = inp.copy()

    # constroí a solução inicial
    stack, reclaim = set_works(file, id, wl, inp, time, routes)
    work = work_time(reclaim, id)

    # salva os dados das melhores soluções encontradas até o momento
    best_dispatch = round(work[1], 1)
    best_solution = stack, reclaim
    best_time = time.copy()
    best_inp = inp.copy()

    count = 0
    while True:
        # escolhe uma linha aleatória da matriz
        line = random.choice(routes)
        swap(line)

        # reseta o tempo e input para calcular novamente com a nova rota
        time = initial_time.copy()
        inp = initial_inp.copy()

        # constroí a solução com a nova rota
        stack, reclaim = set_works(file, id, wl, inp, time, routes)
        work = work_time(reclaim, id)
        dispatch = round(work[1], 1)

        count += 1
        if dispatch < best_dispatch:
            # salva os dados das melhores soluções encontradas até o momento

            best_dispatch = dispatch
            best_solution = stack, reclaim
            best_time = time.copy()
            best_inp = inp.copy()

            # reinicia o contador de iterações
            count = 0

        elif count == 1e4:
            # salva o tempo inicial das máquinas com o melhor resultado
            time = best_time.copy()
            inp = best_inp.copy()
            break

    return best_solution


def swap(route: Union[List[int], Routes]):
    """troca de posição duas linhas da matriz ou duas colunas da lista."""

    size = len(route)
    if size > 1:
        while True:
            i = random.randrange(size)
            j = random.randrange(size)

            if i != j:
                route[i], route[j] = route[j], route[i]
                break


def work_time(reclaims: Works, id: int):
    """calcula o horário em que o pedido foi iniciado e finalizado."""

    try:
        # calcula o horário em que pedido foi iniciado
        start = min([item['start_time'] for item in reclaims
                     if item['output'] is id])

        # calcula o horário em que o pedido foi finalizado
        end = max([item['start_time'] + item['duration']
                   for item in reclaims if item['output'] is id])

    # caso a máquina seja incapaz de retomar o minério
    except ValueError:
        return 0, math.inf

    return start, end