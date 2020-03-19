def debug_print(file: dict):
    print('### STOCKPILES ###')
    for f in file["stockpiles"] : print(f)

    print('### ENGINES ###')
    for f in file["engines"] : print(f)

    print('### INPUTS ###')
    for f in file["inputs"] : print(f)

    print('### OUTPUTS ###')
    for f in file["outputs"] : print(f)

    print('### DISTANCES TRAVEL ###')
    for f in file["distances_travel"] : print(f)

    print('\n### TIME TRAVEL ###')
    for f in file["time_travel"] : print(f)
