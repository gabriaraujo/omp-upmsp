from classes import *
import ujson


def read_file(file_name: str) -> dict:
    """função para realizar a leitura do arquivo de entrada."""

    path = './tests/'
    with open(path + file_name, 'r') as file:
        data = ujson.load(file)

    info = data['info']

    stockpiles = [Stockpile(data['id'],
                            data['position'],
                            data['capacity'],
                            data['engines'],
                            data['weightIni'],
                            [Quality(*q.values()) for q in data['qualityIni']])
                  for data in data['stockpiles']]

    engines = [Engine(data['id'],
                      data['speedStack'],
                      data['speedReclaim'],
                      data['posIni'],
                      data['stockpiles'])
               for data in data['engines']]

    inputs = [Input(data['id'],
                    data['source'],
                    data['weight'],
                    [Quality(*q.values()) for q in data['quality']],
                    data['time'])
              for data in data['inputs']]

    outputs = [Output(data['id'],
                      data['destination'],
                      data['weight'],
                      [Request(*q.values()) for q in data['quality']],
                      data['time'])
               for data in data['outputs']]

    distances_travel = data['distancesTravel']
    time_travel = data['timeTravel']

    result = {
        'info': info,
        'stockpiles': stockpiles,
        'engines': engines,
        'inputs': inputs,
        'outputs': outputs,
        'distances_travel': distances_travel,
        'time_travel': time_travel
    }

    return result


def write_file(path: str, file_name: str, value: dict):
    """função para realizar a gravação do arquivo de saída."""

    with open(path + file_name, 'w') as file:
        ujson.dump(value, file, indent=2)
