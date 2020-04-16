from functions import linear_model
import numpy as np


def solver(file: dict) -> dict:
    """verifica as saídas e combina as pilhas para atender o pedido."""

    # dicionário com resultados do modelo a serem gravados no arquivo .json
    result = {
        'info': file['info'],
        'objective': None,
        'outputs': []
    }

    # resolve o modelo usando programação linear
    result['objective'], weight_list = linear_model(file['outputs'],
                                                    file['stockpiles'],
                                                    file['info'])

    quality_list = [stp.quality_ini for stp in file['stockpiles']]
    weight_list = list(weight_list.values())

    # calcula a qualidade final baseado no peso retirado de cada pilha
    quality_mean = [np.average(quality_list, axis=0, weights=wl)
                    for wl in weight_list]
    quality_mean = [np.array(i).tolist() for i in quality_mean]

    for weight, quality in zip(weight_list, quality_mean):
        result['outputs'].append({'weight': weight,
                                  'quality': quality})

    return result


def set_routes(file: dict) -> [[str]]:
    """define a ordem de funcionamento das máquinas."""

    routes = []
    dist = file['distances_travel']
    for eng in file['engines']:
        # lista para indicar se a máquina já visitou a pilha
        visit = [False] * len(file['stockpiles'])
        visit[eng.pos_ini] = True

        route = [eng.pos_ini]
        pos = eng.pos_ini

        # encontra a pilha mais próxima da máquina e a adiciona na rota
        while not all(visit):
            closer = min(i for i in dist[pos] if i > 0 and
                         visit[dist[pos].index(i)] is False)

            pos = dist[pos].index(closer)
            route.append(pos)
            visit[pos] = True

        # anexa a rota da máquina à lista de rotas
        routes.append(route)

    return set_engines(file, routes)


def set_engines(file: dict, routes: [[int]]) -> [[str]]:
    """define onde cada máquina irá atuar baseado em suas rotas."""

    result = [[] for _ in range(len(file['engines']))]
    visit = [False] * len(file['stockpiles'])

    for rt in zip(*routes):
        for i, r in zip(rt, result):
            if visit[i] is False:
                r.append(str(i))
                visit[i] = True

    return result
