from mip import *
from classes import Output, Stockpile


def linear_model(out: Output, stp: [Stockpile]):
    """resolve o problema de mistura de minérios com programação linear"""

    model = Model("Mistura de Minérios")

    # conjunto de pilhas e teores de qualidade
    p = len(stp)
    t = len(out.quality_goal)

    # quantidade de minérios a produzir e capacidade de cada pilha
    d = out.weight
    q = [stp[i].capacity for i in range(p)]

    # teores de qualidade de cada pilha e seus valores máximos e mínimos
    a = {(i, j): stp[i].quality_ini[j] for i in range(p) for j in range(t)}
    b_min = [out.quality_lower_limit[j] for j in range(t)]
    b_max = [out.quality_upper_limit[j] for j in range(t)]

    # criando variáveis
    # x_i indica a quantidade de minério retirada da pilha i
    x = [model.add_var(name='x_%d' % i) for i in range(p)]

    # criando restrições
    # restrição de demanda
    model += xsum(x[i] for i in range(p)) <= d

    # restrição de capacidade
    for i in range(p):
        model += x[i] <= q[i]

    # restrições de qualidade
    for j in range(t):
        model += xsum(x[i] * a[i, j] for i in range(p)) >= b_min[j]
        model += xsum(x[i] * a[i, j] for i in range(p)) <= b_max[j]

    # resolvendo modelo
    model.optimize()
