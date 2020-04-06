from mip import *
from classes import Output, Stockpile


def linear_model(out: Output, stp: [Stockpile], info: str) -> (float, [float]):
    """resolve o problema de mistura de minérios com programação linear."""

    omp = Model('Ore Mixing Problem')

    # conjunto de pilhas e teores de qualidade
    p = len(stp)
    t = len(out.quality_goal)

    # criando variáveis
    # x_i indica a quantidade de minério retirada da pilha i
    x = [omp.add_var(name='x_%d' % i) for i in range(p)]
    a_max = [omp.add_var(name='a_max_%d' % j) for j in range(t)]
    a_min = [omp.add_var(name='a_min_%d' % j) for j in range(t)]
    b_min = [omp.add_var(name='b_min_%d' % j) for j in range(t)]
    b_max = [omp.add_var(name='b_max_%d' % j) for j in range(t)]

    # criando restrições
    # restrição de demanda
    omp += xsum(x[i] for i in range(p)) == out.weight, f'demand_constr'

    # restrição de capacidade
    for i in range(p):
        omp += x[i] <= stp[i].capacity, f'capacity_constr_{i}'

    # restrições de qualidade
    for j in range(t):
        omp += xsum(x[i] * (stp[i].quality_ini[j] - out.quality_lower_limit[j])
                    for i in range(p)) + a_min[j] * out.weight >= 0, \
               f'min_quality_constr_{j}'
        omp += xsum(x[i] * (stp[i].quality_ini[j] - out.quality_upper_limit[j])
                    for i in range(p)) - a_max[j] * out.weight <= 0, \
               f'max_quality_constr_{j}'
        omp += xsum(x[i] * (stp[i].quality_ini[j] - out.quality_goal[j])
                    for i in range(p)) + b_min[j] - b_max[j] == 0, \
               f'goal_quality_constr_{j}'

    # peso das restrições na função objetivo
    w_1, w_2 = 1e3, 1

    # função objetivo: w_1 * desvio_dos_limites + w_2 * desvio_da_meta
    omp += w_1 * xsum(a_min[j] / sub(out, j, 'lwr') +
                      a_max[j] / sub(out, j, 'upr') for j in range(t)) + \
           w_2 * xsum((b_min[j] + b_max[j]) / min(sub(out, j, 'lwr'),
                                                  sub(out, j, 'upr'))
                      for j in range(t))

    # resolvendo modelo
    omp.write(f'./out/logs/{info}.lp')
    omp.optimize()

    return omp.objective_value, [weight.x for weight in x]


def sub(out: Output, index: int, limit: str) -> float:
    """auxilia no calculo das unidades de desvio e evita divisão por zero."""

    ans = 0
    if limit == 'upr':
        ans = out.quality_upper_limit[index] - out.quality_goal[index]

    elif limit == 'lwr':
        ans = out.quality_goal[index] - out.quality_lower_limit[index]

    return ans if ans != 0 else 1e-6
