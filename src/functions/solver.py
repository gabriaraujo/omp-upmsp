from functions import linear_model
import numpy as np


def solver(file: dict) -> dict:
    """verifica as saídas e combina as pilhas para atender o pedido."""

    # resolve o modelo usando programação linear
    objective, weight_list = linear_model(file['outputs'],
                                          file['stockpiles'],
                                          file['info'])

    quality_mean(file, weight_list)

    return format_file(file, objective)


def format_file(file: dict, objective: float) -> dict:
    """formata os resultados para o modelo de saída do arquivo .json"""

    # dicionário com resultados do modelo a serem gravados no arquivo .json
    result = {
        'info': file['info'],
        'objective': objective,
        'reclaims': [],
        'outputs': []
    }

    requests = [out.quality for out in file['outputs']]
    for req, out in zip(requests, file['outputs']):
        quality_list = [
            {
                'parameter': quality.parameter,
                'value': quality.value,
                'minimum': quality.minimum,
                'maximum': quality.maximum,
                'goal': quality.goal,
                'importance': quality.importance
            } for quality in req]

        result['outputs'].append({'weight': out.weight,
                                  'start_time': 0,
                                  'duration': 0,
                                  'quality': quality_list})

    return result


def quality_mean(file: dict, weight_list: [float]):
    """calcula o valor da qualidade final de cada pedido."""

    weight_list = list(weight_list.values())
    quality_list = [[quality.value for quality in stp.quality_ini]
                    for stp in file['stockpiles']]

    # calcula a qualidade final baseado no peso retirado de cada pilha
    mean = [np.average(quality_list, axis=0, weights=wl) for wl in weight_list]

    # atribui o valor calculado da qualidade ao parâmetro respectivo
    for quality, out in zip(mean, file['outputs']):
        for value, request in zip(quality, out.quality):
            request.value = round(value, 1)


def set_routes(file: dict) -> [[int]]:
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


def set_engines(file: dict, routes: [[int]]) -> [[int]]:
    """define onde cada máquina irá atuar baseado em suas rotas."""

    result = [[] for _ in range(len(file['engines']))]
    visit = [False] * len(file['stockpiles'])

    for rt in zip(*routes):
        for i, r in zip(rt, result):
            if visit[i] is False:
                r.append(i)
                visit[i] = True

    return result
