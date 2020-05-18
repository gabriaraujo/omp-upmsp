from functions import linear_model, set_routes
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

    # lista com os valores empilhados e retirados das pilhas para cada pedido
    stacks, reclaims = zip(*[set_works(file, out.id, wl, input_list, time)
                             for wl, out in zip(weight_list, file['outputs'])])

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

            # calcula o horário em que pedido foi iniciado
            start = min([item['start_time'] for item in reclaims
                         if item['output'] is out.id])

            # calcula o horário em que o pedido foi finalizado
            end = max([item['start_time'] + item['duration']
                       for item in reclaims if item['output'] is out.id])

            # adiciona as informações do pedido na lista de entregas
            outputs.append({'weight': out.weight,
                            'start_time': start,
                            'duration': round(end - start, 1),
                            'quality': quality_list})

    return outputs


def set_works(file: Data,
              id: int,
              wl: List[float],
              inp: List[float],
              time: List[float]) -> Tuple[Works, Works]:
    """define as operações realizadas em cada pilha, a velocidade e o tempo."""

    stacks, reclaims = [], []
    travel = file['time_travel']
    
    for eng, route, in zip(file['engines'], set_routes(file, wl, inp, time)):
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
