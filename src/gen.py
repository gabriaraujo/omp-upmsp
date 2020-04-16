from functions import write_file
import random
import sys


def generate():
    """função para gerar as instâncias e gravar em um arquivo .json"""
    write_file('./tests/', sys.argv[1], instance_gen(sys.argv[2:]))


def instance_gen(args: [str]) -> dict:
    """gerador de instâncias pseudo-aleatórias."""

    # converte todos os parametros para os tipos corretos
    argc = len(args)
    name = args[0] if argc > 0 else f'Instance_R{random.randint(1, 1e3)}'
    stockpiles = int(args[1]) if argc > 1 else 4
    capacity = float(args[2]) if argc > 2 else 400
    outputs = int(args[3]) if argc > 3 else 1
    weight = float(args[4]) if argc > 4 else 1000
    inputs = int(args[5]) if argc > 5 else 1
    engines = int(args[6]) if argc > 6 else 2
    variant = float(args[7]) if argc > 7 else 0.2

    # cria um dicionário para salvar os dados gerados
    instance = {'info': name}

    # valores de variação inferior e superior das medidas
    lb = 1 - variant
    ub = 1 + variant

    # capacidade máxima de cada pilha
    cpty = [round(random.uniform(lb * capacity, ub * capacity), 1)
            for _ in range(stockpiles)]

    # gera os valores para as pilhas de minério
    instance['stockpiles'] = [{
        'id': str(i + 1),
        'position': i,
        'capacity': cpty[i],
        'engines': [str(eng + 1) for eng in range(engines)],
        'weightIni': round(random.uniform(lb * cpty[i], cpty[i]), 1),
        'qualityIni': gen_quality(lb, ub)
    } for i in range(stockpiles)]

    # gera os valores para os equipamentos
    stp = [i for i in range(stockpiles)]
    random.shuffle(stp)
    instance['engines'] = [{
        'id': str(i + 1),
        'speedStack': round(random.uniform(20, 50), 1),
        'speedReclaim': round(random.uniform(20, 50), 1),
        'posIni': stp.pop(),
        'stockpiles': [str(j + 1) for j in range(stockpiles)]
    } for i in range(engines)]

    # gera os valores para a entrada de minérios
    src = random.randrange(1, stockpiles)
    instance['inputs'] = [{
        'id': str(i + 1),
        'source': str(src),
        'weight': round(variant * cpty[src], 1),
        'quality': gen_quality(lb, ub),
        'time': round(random.uniform(0, 10), 1)
    } for i in range(inputs)]

    # gera os valores de cada pedido
    instance['outputs'] = [{
        'id': str(i + 1),
        'destination': str(i + 1),
        "weight": round(random.uniform(lb * weight, ub * weight), 1),
        "qualityGoal": [
            round(random.uniform(55, 100), 2),
            round(random.uniform(0, 1.5), 2),
            round(random.uniform(0, 0.5), 2),
            round(random.uniform(0, 0.5), 2),
            round(random.uniform(0, 1), 2),
            round(random.uniform(3.5, 5), 2)
        ],
        "qualityUpperLimit": [100, 1.5, 0.5, 0.5, 1.0, 5],
        'qualityLowerLimit': [55, 0, 0, 0, 0, 3.5],
        "time": round(random.uniform(0, 10), 1)
    } for i in range(outputs)]

    # gera as distâncias entre as pilhas
    instance['distancesTravel'] = [
        [float(abs(i - j)) for i in range(stockpiles)]
        for j in range(stockpiles)
    ]

    # gera os tempos de locomoção entre as pilhas
    instance['timeTravel'] = [
        [(abs(i - j) * 20.0 + 10.0) for i in range(stockpiles)]
        for j in range(stockpiles)
    ]

    return instance


def gen_quality(lb: float, ub: float) -> [float]:
    """gera a qualidade inicial para cada pilha de minério."""

    return [
        round(random.uniform(55 * lb, 100), 2),
        round(random.uniform(0, 1.5 * ub), 2),
        round(random.uniform(0, 5 * ub), 2),
        round(random.uniform(0, 5 * ub), 2),
        round(random.uniform(0, 1 * ub), 2),
        round(random.uniform(3.5 * lb, 5 * ub), 2)
    ]


if __name__ == '__main__':
    generate()
