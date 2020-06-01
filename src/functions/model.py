from mip import *
from config import *


def linear_model(out: Outputs,
                 stp: Stockpiles,
                 inp: Inputs,
                 info: str) -> Solution:
    """resolve o problema de mistura de minérios com programação linear."""

    omp = Model('Ore Mixing Problem')

    # conjunto de pilhas, teores de qualidade, pedidos e entradas
    p = len(stp)
    t = len(out[0].quality)
    r = len(out)
    e = len(inp)

    # criando variáveis
    # x_ik indica a quantidade de minério retirada da pilha i para o pedido k
    x = {(i, k): omp.add_var(name=f'x_{i}{k}')
         for i in range(p) for k in range(r)}

    # y_hi indica a quantidade de minério retirada do input h para a pilha i
    y = {(h, i): omp.add_var(name=f'y_{h}{i}')
         for h in range(e) for i in range(p)}

    # var_jk indica o teor de qualidade j do pedido k
    a_max = {(j, k): omp.add_var(name=f'a_max_{j}{k}')
             for j in range(t) for k in range(r)}
    a_min = {(j, k): omp.add_var(name=f'a_min_{j}{k}')
             for j in range(t) for k in range(r)}
    b_min = {(j, k): omp.add_var(name=f'b_min_{j}{k}')
             for j in range(t) for k in range(r)}
    b_max = {(j, k): omp.add_var(name=f'b_max_{j}{k}')
             for j in range(t) for k in range(r)}

    # restrição de capacidade das entradas
    for h in range(e):
        omp += xsum(y[h, i] for i in range(p)) <= inp[h].weight, \
            f'input_weight_constr_{h}'

    # restrição de capacidade das pilhas
    for i in range(p):
        omp += xsum(y[h, i] for h in range(e)) + stp[i].weight_ini \
            <= stp[i].capacity, f'capacity_constr_{i}'

        for h in range(e):
            omp += xsum(x[i, k] for k in range(r)) \
                <= stp[i].weight_ini + y[h, i], f'weight_constr_{i}{h}'

    # criando restrições
    for k in range(r):
        # restrição de demanda
        omp += xsum(x[i, k] for i in range(p)) == out[k].weight, \
            f'demand_constr_{k}'

        # restrições de qualidade
        for j in range(t):
            # restrição de desvio da qualidade mínima
            q_1 = xsum(x[i, k] * (stp[i].quality_ini[j].value -
                                  out[k].quality[j].minimum) for i in range(p))

            omp += q_1 + a_min[j, k] * out[k].weight >= 0, \
                f'min_quality_constr_{j}{k}'

            # restrição de desvio da qualidade máxima
            q_2 = xsum(x[i, k] * (stp[i].quality_ini[j].value -
                                  out[k].quality[j].maximum) for i in range(p))

            omp += q_2 - a_max[j, k] * out[k].weight <= 0, \
                f'max_quality_constr_{j}{k}'

            # restrição de desvio da meta de qualidade
            q_3 = xsum(x[i, k] * (stp[i].quality_ini[j].value -
                                  out[k].quality[j].goal) for i in range(p))

            omp += q_3 + (b_min[j, k] - b_max[j, k]) * out[k].weight == 0, \
                f'goal_quality_constr_{j}{k}'

    # peso das restrições na função objetivo
    w_1, w_2 = 1e3, 1

    # desvio dos limites
    d_limit = xsum(out[k].quality[j].importance *
                   a_min[j, k] / normalize(out, j, k, 'lb') +
                   out[k].quality[j].importance *
                   a_max[j, k] / normalize(out, j, k, 'ub')
                   for j in range(t) for k in range(r))

    # desvio da meta
    d_goal = xsum((b_min[j, k] + b_max[j, k]) /
                  min(normalize(out, j, k, 'lb'), normalize(out, j, k, 'ub'))
                  for j in range(t) for k in range(r))

    # função objetivo: w_1 * desvio_dos_limites + w_2 * desvio_da_meta
    omp += w_1 * d_limit + w_2 * d_goal

    # resolvendo modelo
    omp.write(f'./out/logs/{info}.lp')
    omp.optimize()

    if omp.num_solutions > 0:
        # dicionário com as massas retiradas de cada pilha i para cada pedido k
        reclaims = {
            f'id: {out[k].id}': [x[i, k].x for i in range(p)] for k in range(r)
        }

        # dicionário com as massas retiradas de cada input j para cada pilha i
        inputs = {
            f'id: {stp[i].id}': [y[h, i].x for h in range(e)] for i in range(p)
        }

        return omp.objective_value, inputs, reclaims

    else:
        return None, {}, {
            f'id: {out[k].id}': [0 for _ in range(p)] for k in range(r)
        }


def normalize(out: Outputs, j: int, k: int, bound: str) -> float:
    """auxilia no calculo das unidades de desvio e evita divisão por zero."""

    # out[k].quality[j] indica o teor de qualidade j do pedido k
    ans = 0

    # ub indica que o cálculo deve ser normalizado feito pela qualidade máxima
    if bound == 'ub':
        ans = out[k].quality[j].maximum - out[k].quality[j].goal

    # lb indica que o cálculo deve ser normalizado feito pela qualidade mínima
    elif bound == 'lb':
        ans = out[k].quality[j].goal - out[k].quality[j].minimum

    return ans if ans != 0 else 1e-6
