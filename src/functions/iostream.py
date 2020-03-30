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
                            [int(i) for i in data['engines']],
                            data['weightIni'],
                            data['qualityIni'])
                  for data in data['stockpiles']]

    engines = [Engine(data['id'],
                      data['speedStack'],
                      data['speedReclaim'],
                      data['posIni'],
                      [int(i) for i in data['stockpiles']])
               for data in data['engines']]

    inputs = [Input(data['id'],
                    data['source'],
                    data['weight'],
                    data['quality'],
                    data['time'])
              for data in data['inputs']]

    outputs = [Output(data['id'],
                      data['destination'],
                      data['weight'],
                      data['qualityGoal'],
                      data['qualityUpperLimit'],
                      data['qualityLowerLimit'],
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


def write_file(file_name: str, value: dict):
    """função para realizar a gravação do arquivo de saída."""

    path = './out/json/'
    with open(path + file_name, 'w') as file:
        ujson.dump(value, file, indent=2)
