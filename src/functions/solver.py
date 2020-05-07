from functions import linear_model
import numpy as np


def solver(file: dict) -> dict:
    """verifica as saídas e combina as pilhas para atender o pedido."""

    # resolve o modelo usando programação linear
    objective, weight_list = linear_model(file['outputs'],
                                          file['stockpiles'],
                                          file['info'])

    # converte o dicionário com os pesos de cada pedido em um lista de listas
    weight_list = list(weight_list.values())

    # lista com o tempo de início de trabalho de cada máquina
    start_time = [0] * len(file['engines'])

    # gera uma lista com os valores retirados das pilhas para cada pedido
    reclaims = [set_reclaims(file, out.id, wl, start_time)
                for wl, out in zip(weight_list, file['outputs'])]

    # transforma o resultado em uma única lista
    reclaims = [item for sublist in reclaims for item in sublist]

    # altera os valores de qualidade obtidos de cada parâmetro para cada pedido
    quality_mean(file, weight_list)

    return format_file(file, objective, reclaims)


def format_file(file: dict, objective: float, reclaims: [dict]) -> dict:
    """formata os resultados para o modelo de saída do arquivo .json"""

    # dicionário com resultados do modelo a serem gravados no arquivo .json
    result = {
        'info': file['info'],
        'objective': objective,
        'reclaims': reclaims,
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


def quality_mean(file: dict, weight_list: [[float]]):
    """calcula o valor da qualidade final de cada pedido."""

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
    distances = file['distances_travel']
    for eng in file['engines']:
        # lista para indicar se a máquina já visitou a pilha
        visited = [False] * len(file['stockpiles'])
        visited[eng.pos_ini] = True

        route = [eng.pos_ini]
        pos = eng.pos_ini

        # encontra a pilha mais próxima da máquina e a adiciona na rota
        while not all(visited):
            closer = min(dist for dist, is_visited in
                         zip(distances[pos], visited)
                         if dist > 0 and is_visited is False)

            pos = distances[pos].index(closer)
            route.append(pos)
            visited[pos] = True

        # anexa a rota da máquina à lista de rotas
        routes.append(route)

    return set_engines(file, routes)


def set_engines(file: dict, routes: [[int]]) -> [[int]]:
    """define onde cada máquina irá atuar baseado em suas rotas."""

    # result salva as lista de pilhas visitadas por cada máquina
    result = [[] for _ in range(len(file['engines']))]
    visited = [False] * len(file['stockpiles'])

    # t_stp é uma tupla das pilhas a serem visitadas por cada máquina
    for t_stp in zip(*routes):
        for stp, r in zip(t_stp, result):
            if not visited[stp]:
                r.append(stp)
                visited[stp] = True

    return result


def set_reclaims(file: dict, id: int, wl: [float], time: [float]) -> [dict]:
    """define quanto vai ser tirado de cada pilha, a velocidade e o tempo."""

    reclaims = []
    for eng, route, in zip(file['engines'], set_routes(file)):
        eng_index = file['engines'].index(eng)

        for stp in route:
            duration = round(wl[stp] / eng.speed_reclaim, 1)
            reclaims.append({
                "weight": round(wl[stp], 1),
                "stockpile": stp,
                "engine": eng.id,
                "start_time": time[eng_index],
                "duration": duration,
                "output": id
            }) if wl[stp] > 0 else None
            time[eng_index] += duration

    return reclaims
