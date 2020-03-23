from src.classes import *


def solver(file: dict) -> [(float, [float])]:
    """verifica as saídas e combina as pilhas para atender o pedido."""

    result = []
    for out in file["outputs"]:
        curr_weight = 0
        curr_quality = [0, 0, 0, 0, 0, 0]

        for stp in file["stockpiles"]:
            if check_quality(stp.quality_ini,
                             out.quality_lower_limit,
                             out.quality_upper_limit):
                curr_weight += mixing(curr_weight, curr_weight, stp, out)

        r = curr_weight, curr_quality
        result.append(r)

    return result


def check_quality(ini: [int], lower_limit: [int], upper_limit: [int]) -> bool:
    """verifica se a qualidade está dentro dos limites."""

    for (init, lower, upper) in zip(ini, lower_limit, upper_limit):
        if init < lower or init > upper: return False

    return True


def mixing(wt: float, quality: [float], stp: Stockpile, out: Output) -> float:
    """calcula a média entre a qualidade atual e a recebida."""

    diff = out.weight - wt
    if 0 < diff < stp.weight_ini:
        quality = quality_mean(wt, diff, quality, stp.quality_ini)
        wt += diff
        stp.weight_ini -= diff

    elif diff > 0 and stp.weight_ini < diff:
        quality = quality_mean(wt, stp.weight_ini, quality, stp.quality_ini)
        wt += stp.weight_ini
        stp.weight_ini = 0

    return wt


def quality_mean(wi: float, wr: float, qi: [float], qr: [float]) -> [float]:
    """calcula a média pondera das qualidades."""

    result = []
    for (ini, rec) in zip(qi, qr):
        r = (ini * wi + rec * wr) / (wi + wr)
        result.append(r)

    return result
