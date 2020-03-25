from functions import quality_print, linear_model
from classes import Output, Stockpile
import numpy as np


def solver(file: dict) -> [(float, [float])]:
    """verifica as saídas e combina as pilhas para atender o pedido."""

    result = []
    for out in file["outputs"]:
        curr_weight = 0
        curr_quality = []

        # resolve o modelo usando programação linear
        linear_model(out, file["stockpiles"])

        # retira-se o minério de cada pilha para completar a demanda
        for stp in file["stockpiles"]:
            if curr_weight < out.weight:
                curr_weight = mixing(curr_weight, curr_quality, out, stp)

        # calcula os parâmetros de qualidade obtidos
        quality = quality_mean(curr_quality)

        # imprime a qualidade obtida e os limites superior e inferior
        quality_print(quality,
                      out.quality_lower_limit,
                      out.quality_upper_limit)

        # verifica se a qualidade obtida está dentro dos limites desejados
        if check_quality(quality,
                         out.quality_lower_limit,
                         out.quality_upper_limit):
            result.append((curr_weight, quality))

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
    if 0 < diff <= stp.weight_ini:
        qw.append((diff, stp.quality_ini))
        cw += diff
        stp.weight_ini -= diff

    elif diff > 0 and diff > stp.weight_ini:
        qw.append((stp.weight_ini, stp.quality_ini))
        cw += stp.weight_ini
        stp.weight_ini = 0

    return cw


def quality_mean(cq: [(float, [float])]) -> [float]:
    """separa a lista de qualidade e pesos para calcular a média ponderada"""

    quality_weights = [qw[0] for qw in cq]
    quality_list = [ql[1] for ql in cq]

    return np.average(quality_list, axis=0, weights=quality_weights)
