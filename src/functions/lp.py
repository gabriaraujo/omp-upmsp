from mip import *
from classes import Output, Stockpile


def linear_model(out: [Output], stp: [Stockpile], info: str) -> (float, dict):
    """resolve o problema de mistura de minérios com programação linear."""

    omp = Model('Ore Mixing Problem')

    # conjunto de pilhas, teores de qualidade e pedidos
    p = len(stp)
    t = len(out[0].quality_goal)
    r = len(out)

    # criando variáveis
    # x_ik indica a quantidade de minério retirada da pilha i para o pedido k
    x = {(i, k): omp.add_var(name=f'x_{i}{k}')
         for i in range(p) for k in range(r)}

    # var_jk indica o teor de qualidade j do pedido k
    a_max = {(j, k): omp.add_var(name=f'a_max_{j}{k}')
             for j in range(t) for k in range(r)}
    a_min = {(j, k): omp.add_var(name=f'a_min_{j}{k}')
             for j in range(t) for k in range(r)}
    b_min = {(j, k): omp.add_var(name=f'b_min_{j}{k}')
             for j in range(t) for k in range(r)}
    b_max = {(j, k): omp.add_var(name=f'b_max_{j}{k}')
             for j in range(t) for k in range(r)}

    # restrição de capacidade
    for i in range(p):
        omp += xsum(x[i, k] for k in range(r)) <= stp[i].weight_ini, \
            f'capacity_constr_{i}'

    # criando restrições
    for k in range(r):
        # restrição de demanda
        omp += xsum(x[i, k] for i in range(p)) == out[k].weight, \
               f'demand_constr_{k}'

        # restrições de qualidade
        for j in range(t):
            omp += xsum(x[i, k] * (stp[i].quality_ini[j] -
                                   out[k].quality_lower_limit[j])
                        for i in range(p)) + a_min[j, k] * out[k].weight >= 0, \
                f'min_quality_constr_{j}{k}'

            omp += xsum(x[i, k] * (stp[i].quality_ini[j] -
                                   out[k].quality_upper_limit[j])
                        for i in range(p)) - a_max[j, k] * out[k].weight <= 0, \
                f'max_quality_constr_{j}{k}'

            omp += xsum(x[i, k] * (stp[i].quality_ini[j] -
                                   out[k].quality_goal[j])
                        for i in range(p)) + b_min[j, k] - b_max[j, k] == 0, \
                f'goal_quality_constr_{j}{k}'

    # peso das restrições na função objetivo
    w_1, w_2 = 1e3, 1

    # função objetivo: w_1 * desvio_dos_limites + w_2 * desvio_da_meta
    omp += w_1 * xsum(a_min[j, k] / sub(out, j, k, 'lwr') +
                      a_max[j, k] / sub(out, j, k, 'upr')
                      for j in range(t) for k in range(r)) \
        + w_2 * xsum((b_min[j, k] + b_max[j, k]) / min(sub(out, j, k, 'lwr'),
                                                       sub(out, j, k, 'upr'))
                     for j in range(t) for k in range(r))

    # resolvendo modelo
    omp.write(f'./out/logs/{info}.lp')
    omp.optimize()

    # dicionário com as massas retiradas de cada pilha i para cada pedido k
    weights = {
        f'id: {out[k].id}': [x[i, k].x for i in range(p)] for k in range(r)
    }

    return omp.objective_value, weights


def sub(out: [Output], j: int, k: int, limit: str) -> float:
    """auxilia no calculo das unidades de desvio e evita divisão por zero."""

    ans = 0
    if limit == 'upr':
        ans = out[k].quality_upper_limit[j] - out[k].quality_goal[j]

    elif limit == 'lwr':
        ans = out[k].quality_goal[j] - out[k].quality_lower_limit[j]

    return ans if ans != 0 else 1e-6
