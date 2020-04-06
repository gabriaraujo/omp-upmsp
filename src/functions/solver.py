from functions import linear_model
from classes import Output, Stockpile
import numpy as np


def solver(file: dict) -> dict:
    """verifica as saídas e combina as pilhas para atender o pedido."""

    # dicionário com resultados do modelo a serem gravados no arquivo .json
    result = {
        'info': file['info'],
        'objective': None,
        'outputs': []
    }

    for out in file['outputs']:
        # resolve o modelo usando programação linear
        result['objective'], weight_list = linear_model(out,
                                               file['stockpiles'],
                                               file['info'])

        quality_list = [stp.quality_ini for stp in file['stockpiles']]

        # calcula a qualidade final baseado no peso retirado de cada pilha
        quality = np.average(quality_list, axis=0, weights=weight_list)
        quality = np.array(quality).tolist()

        result['outputs'].append({'weight': weight_list,
                                  'quality': quality})

    return result
