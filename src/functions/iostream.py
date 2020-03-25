from classes import *
import ujson


def read_file(file_name: str) -> dict:
    """função para realizar a leitura do arquivo de entrada."""

    with open(file_name, "r") as file:
        data_store = ujson.loads(file.read())

    stockpiles = [Stockpile(data["id"],
                            data["position"],
                            data["capacity"],
                            [int(i) for i in data["engines"]],
                            data["weightIni"],
                            data["qualityIni"])
                  for data in data_store["stockpiles"]]

    engines = [Engine(data["id"],
                      data["speedStack"],
                      data["speedReclaim"],
                      data["posIni"],
                      [int(i) for i in data["stockpiles"]])
               for data in data_store["engines"]]

    inputs = [Input(data["id"],
                    data["source"],
                    data["weight"],
                    data["quality"],
                    data["time"])
              for data in data_store["inputs"]]

    outputs = [Output(data["id"],
                      data["destination"],
                      data["weight"],
                      data["qualityGoal"],
                      data["qualityUpperLimit"],
                      data["qualityLowerLimit"],
                      data["time"])
               for data in data_store["outputs"]]

    distances_travel = data_store["distancesTravel"]
    time_travel = data_store["timeTravel"]

    result = {
        "stockpiles": stockpiles,
        "engines": engines,
        "inputs": inputs,
        "outputs": outputs,
        "distances_travel": distances_travel,
        "time_travel": time_travel
    }

    return result
