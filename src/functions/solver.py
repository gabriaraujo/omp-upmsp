from functions import quality_print, linear_model
from classes import Output, Stockpile
import numpy as np


def solver(file: dict) -> dict:
    """verifica as saídas e combina as pilhas para atender o pedido."""

    # dicionário com resultados do modelo a serem gravados no arquivo .json
    result = {
        'info': file['info'],
        'objective': None,
        'outputs': []
    }

    for out in file['outputs']:
        # resolve o modelo usando programação linear
        result['objective'] = linear_model(out,
                                           file['stockpiles'],
                                           file['info'])

        # retira-se o minério de cada pilha para completar a demanda
        cw, cq = 0, []
        for stp in file['stockpiles']:
            cw = mixing(cw, cq, out, stp)

        # calcula os parâmetros de qualidade obtidos
        weight = [w[0] for w in cq]
        quality = quality_mean(cq)

        result['outputs'].append({'weight': weight,
                                  'quality': quality})

    return result


def check_quality(q: [int], lb: [int], ub: [int]) -> bool:
    """verifica se a qualidade está dentro dos limites."""

    for (quality, lower, upper) in zip(q, lb, ub):
        if not lower <= quality <= upper: return False

    return True


def mixing(cw: float,
           qw: [(float, [float])],
           out: Output,
           stp: Stockpile) -> float:
    """separa os pesos e qualidade de cada pilha para atender a demanda"""

    diff = out.weight - cw
    if 0 <= diff < stp.weight_ini:
        qw.append((diff, stp.quality_ini))
        cw += diff
        stp.weight_ini -= diff

    elif diff >= stp.weight_ini:
        qw.append((stp.weight_ini, stp.quality_ini))
        cw += stp.weight_ini
        stp.weight_ini = 0

    return cw


def quality_mean(cq: [(float, [float])]) -> [float]:
    """separa a lista de qualidade e pesos para calcular a média ponderada"""

    quality_weights = [qw[0] for qw in cq]
    quality_list = [ql[1] for ql in cq]

    mean = np.average(quality_list, axis=0, weights=quality_weights)
    mean = np.array(mean).tolist()

    return mean
