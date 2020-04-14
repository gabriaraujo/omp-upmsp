import sys
import ujson
import random


def generate():
    """função para gerar as instâncias e gravar em um arquivo .json"""
    write_file(sys.argv[1], instance_gen(*sys.argv[2:]))


def write_file(file_name: str, value: dict):
    """função para realizar a gravação do arquivo de saída."""

    path = './tests/'
    with open(path + file_name, 'w') as file:
        ujson.dump(value, file, indent=2)


def instance_gen(name: str = f'Instance_R{random.randint(1, 1e3)}',
                 stockpiles: int = 4,
                 capacity: float = 400,
                 outputs: int = 1,
                 weight: float = 1000,
                 inputs: int = 1,
                 engines: int = 2,
                 variant: float = 0.2) -> dict:
    """gerador de instâncias pseudo-aleatórias."""

    # converte todos os parametros para os tipos corretos
    stockpiles = int(stockpiles)
    capacity = float(capacity)
    outputs = int(outputs)
    weight = float(weight)
    inputs = int(inputs)
    engines = int(engines)
    variant = float(variant)

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
    instance['engines'] = [{
        'id': str(i + 1),
        'speedStack': round(random.uniform(20, 50), 1),
        'speedReclaim': round(random.uniform(20, 50), 1),
        'posIni': random.randrange(stockpiles),
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
