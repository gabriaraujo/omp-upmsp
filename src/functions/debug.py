def file_print(file: dict):
    """função para imprimir os dados recebidos do arquivo de entrada."""

    print('### STOCKPILES ###')
    for elem in file['stockpiles']: print(elem)

    print('### ENGINES ###')
    for elem in file['engines']: print(elem)

    print('### INPUTS ###')
    for elem in file['inputs']: print(elem)

    print('### OUTPUTS ###')
    for elem in file['outputs']: print(elem)

    print('### DISTANCES TRAVEL ###')
    for elem in file['distances_travel']: print(elem)

    print('\n### TIME TRAVEL ###')
    for elem in file['time_travel']: print(elem)


def quality_print(cq: [float], lb: [float], ub: [float]):
    """função para imprimir os parâmetros de qualidade desejados e o obtido."""

    print('ub: ', ['%6.2f' % elem for elem in ub])
    print('cq: ', ['%6.2f' % elem for elem in cq])
    print('lb: ', ['%6.2f' % elem for elem in lb])
