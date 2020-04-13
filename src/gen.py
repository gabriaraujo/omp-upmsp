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
                 capacity: int = 400,
                 outputs: int = 1,
                 weight: int = 1000,
                 inputs: int = 1,
                 engines: int = 2,
                 variant: float = 0.2) -> dict:
    """gerador de instâncias aleatórias."""

    stockpiles = int(stockpiles)
    capacity = int(capacity)
    outputs = int(outputs)
    weight = int(weight)
    inputs = int(inputs)
    engines = int(engines)
    variant = float(variant)

    ub = 1 + variant
    lb = 1 - variant
    cpty = [random.randint(int(lb * capacity), int(ub * capacity))
            for _ in range(stockpiles)]
    stp = [{
        'id': str(i + 1),
        'position': i,
        'capacity': cpty[i],
        'engines': [str(eng + 1) for eng in range(engines)],
        'weightIni': random.randint(int(lb * cpty[i]), cpty[i]),
        'qualityIni': [
            round(random.uniform(55 * lb, 100), 2),
            round(random.uniform(0, 1.5 * ub), 2),
            round(random.uniform(0, 5 * ub), 2),
            round(random.uniform(0, 5 * ub), 2),
            round(random.uniform(0, 1 * ub), 2),
            round(random.uniform(3.5 * lb, 5 * ub), 2)
        ]
    } for i in range(stockpiles)]

    eng = [{
        'id': str(i + 1),
        'speedStack': round(random.uniform(20, 50), 1),
        'speedReclaim': round(random.uniform(20, 50), 1),
        'posIni': random.randrange(stockpiles),
        'stockpiles': [str(j + 1) for j in range(stockpiles)]
    } for i in range(engines)]

    src = random.randrange(1, stockpiles)
    inp = [{
        'id': str(i + 1),
        'source': str(src),
        'weight': variant * cpty[src],
        'quality': [
            round(random.uniform(55 * lb, 100), 2),
            round(random.uniform(0, 1.5 * ub), 2),
            round(random.uniform(0, 5 * ub), 2),
            round(random.uniform(0, 5 * ub), 2),
            round(random.uniform(0, 1 * ub), 2),
            round(random.uniform(3.5 * lb, 5 * ub), 2)
        ],
        'time': round(random.uniform(0, 10), 1)
    } for i in range(inputs)]

    out = [{
        'id': str(i + 1),
        'destination': str(i + 1),
        "weight": random.randint(int(lb * weight), int(ub * weight)),
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

    dist = [
        [float(abs(i - j)) for i in range(stockpiles)]
        for j in range(stockpiles)
    ]

    time = [
        [(abs(i - j) * 20.0 + 10.0) for i in range(stockpiles)]
        for j in range(stockpiles)
    ]

    instance = {
        'info': name,
        'stockpiles': stp,
        'engines': eng,
        'inputs': inp,
        'outputs': out,
        'distancesTravel': dist,
        'timeTravel': time
    }

    return instance


if __name__ == '__main__':
    generate()
