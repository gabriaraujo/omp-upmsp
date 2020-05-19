from functions import linear_model, set_routes, local_search, work_time
from config import *
import numpy as np


def solver(file: Data) -> Result:
    """combina as pilhas para atender o pedido."""

    # resolve o modelo usando programação linear
    objective, input_dict, weight_dict = linear_model(file['outputs'],
                                                      file['stockpiles'],
                                                      file['inputs'],
                                                      file['info'])

    # converte os dicionários com os pesos de cada pedido em um lista de listas
    weight_list = list(weight_dict.values())
    input_list = [sum(inp) for inp in list(input_dict.values())]

    # lista com o tempo de início de trabalho de cada máquina
    time = [0] * len(file['engines'])

    stacks, reclaims = [], []
    for wl, out in zip(weight_list, file['outputs']):
        routes = set_routes(file, wl, input_list, time)

        # realiza a busca local
        solution = local_search(file, out.id, wl, input_list, time, routes)

        stacks.append(solution[0])
        reclaims.append(solution[1])

    # transforma o resultado em uma única lista
    reclaims = [item for sublist in reclaims for item in sublist]
    stacks = [item for sublist in stacks for item in sublist]

    # altera os valores de qualidade obtidos de cada parâmetro para cada pedido
    quality_mean(file, weight_list)
    outputs = set_outputs(file, objective, reclaims)

    return {
        'info': file['info'],
        'objective': objective,
        'stacks': stacks,
        'reclaims': reclaims,
        'outputs': outputs
    }


def quality_mean(file: Data, weight_list: List[List[float]]):
    """calcula o valor da qualidade final de cada pedido."""

    quality_list = [[quality.value for quality in stp.quality_ini]
                    for stp in file['stockpiles']]

    try:
        # calcula a qualidade final baseado no peso retirado de cada pilha
        mean = [np.average(quality_list, axis=0, weights=wl)
                for wl in weight_list]

        # atribui o valor calculado da qualidade ao parâmetro respectivo
        for quality, out in zip(mean, file['outputs']):
            for value, request in zip(quality, out.quality):
                request.value = round(value, 1)

    # caso o modelo seja inviável, a função np.average() lança uma exceção
    except ZeroDivisionError:
        pass


def set_outputs(file: Data, objective: float, reclaims: Works) -> Deliveries:
    """salva os dados de saída de cada pedido."""

    outputs = []
    # caso o modelo não seja inviável
    if objective is not None:

        # percorre a lista de pedidos para salvar os dados de qualidade
        requests = [out.quality for out in file['outputs']]
        for req, out in zip(requests, file['outputs']):
            # salva os dados da qualidade para cada parâmetro de cada pedido
            quality_list = [
                {
                    'parameter': quality.parameter,
                    'value': quality.value,
                    'minimum': quality.minimum,
                    'maximum': quality.maximum,
                    'goal': quality.goal,
                    'importance': quality.importance
                } for quality in req]

            # calcula o horário em que o pedido foi iniciado e finalizado
            start, end = work_time(reclaims, out.id)

            # adiciona as informações do pedido na lista de entregas
            outputs.append({'weight': out.weight,
                            'start_time': start,
                            'duration': round(end - start, 1),
                            'quality': quality_list})

    return outputs
