from mip import *
from classes import Output, Stockpile


def linear_model(out: Output, stp: [Stockpile], info: str) -> float:
    """resolve o problema de mistura de minérios com programação linear."""

    omp = Model('Mistura de Minérios')

    # conjunto de pilhas e teores de qualidade
    p = len(stp)
    t = len(out.quality_goal)

    # criando variáveis
    # x_i indica a quantidade de minério retirada da pilha i
    x = [omp.add_var(name='x_%d' % i) for i in range(p)]
    a_max = [omp.add_var(name='a_max_%d' % j) for j in range(t)]
    a_min = [omp.add_var(name='a_min_%d' % j) for j in range(t)]

    # criando restrições
    # restrição de demanda
    omp += xsum(x[i] for i in range(p)) == out.weight

    # restrição de capacidade
    for i in range(p):
        omp += x[i] <= stp[i].capacity

    # restrições de qualidade
    for j in range(t):
        omp += xsum(x[i] * (stp[i].quality_ini[j] - out.quality_lower_limit[j])
                    for i in range(p)) + a_min[j] * out.weight >= 0
        omp += xsum(x[i] * (stp[i].quality_ini[j] - out.quality_upper_limit[j])
                    for i in range(p)) - a_max[j] * out.weight <= 0

    # função objetivo
    omp += xsum(a_max[j] / safe_sub(out.quality_goal[j],
                                    out.quality_lower_limit[j]) +
                a_min[j] / safe_sub(out.quality_upper_limit[j],
                                    out.quality_goal[j])
                for j in range(t))

    # resolvendo modelo
    omp.write(f'./out/logs/{info}.lp')
    omp.optimize()

    return omp.objective_value


def safe_sub(x: float, y: float) -> float:
    """função para evitar erro de divisão por zero no somatório do modelo."""

    ans = x - y
    return ans if ans != 0 else 1
