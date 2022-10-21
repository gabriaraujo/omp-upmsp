from config import Objective, Parmeters
from algorithm.constructive import Constructive, LinModel, PreModel, PostModel
from algorithm.neighborhood import Shift, SimpleSwap, Swap, Switch, \
    SmartSimpleSwap, SmartShift, SmartSwap, SmartSwitch
from algorithm.heuristic import Heuristic, SA, LAHC
from model.problem import Problem
from model.solution import Solution
from typing import List, Optional
import random
import sys
import time

def main():
    """This is the main function of the program, responsible of parsing the 
    input, instantiating moves and heuristics and printing the results.
    """
    parms: Parmeters = {
        'constructive': 'postmodel',
        'algorithm': '',
        'feedback': 0,
        'seed': 0,
        'maxiters': int(1e3),
        'lsize': int(1e3),
        'alpha': 0.9,
        'samax': int(1e3),
        't0': 1.0
    }

    read_args(sys.argv, parms)
    
    random.seed(parms['seed'])
    problem: Problem = Problem('./tests/' + sys.argv[1])
    solution: Solution = Solution(problem)
    model: LinModel = LinModel(problem)

    constructive: Constructive = construct(problem, solution, model, parms)

    solver: Optional[Heuristic] = None
    if parms['algorithm'] != '':
        solver = solve(problem, solution, constructive, parms)
        solution = solver.best_solution

    if parms['feedback'] > 0: 
        feedback_approach(solution, model, solver, constructive, parms)

    solution.set_deliveries()
    solution.write('./out/json/' + sys.argv[2])


def construct(
    problem: Problem, 
    solution: Solution,
    model: LinModel,
    parms: Parmeters
) -> Constructive:
    """This function executes the selected constructive method.

    Args:
        problem (Problem): The problem reference.
        solution (Solution): The solution reference.
        parms (Parmeters): The operating guidelines.

    Returns:
        Constructive: The constructive procedure.
    """
    constructive: Constructive

    if parms['constructive'] != 'premodel' \
    and parms['constructive'] != 'postmodel':
        print_usage(parms)

    elif parms['constructive'] == 'premodel': 
        reclaims = {
            f'id: {k.id}': [i.weight_ini for i in problem.stockpiles] 
                for k in problem.outputs
        }

        inputs = {
            f'id: {k.id}': [i.weight for i in problem.inputs] 
                for k in problem.stockpiles
        }

        objective: Objective = (None, reclaims, inputs)
        solution.set_objective(objective)

        constructive = PreModel(problem, solution)
        constructive.run()

        model.add_weights('x', list(constructive._feed_back))
        model.add_weights('y', list(constructive._feed_back))

    objective: Objective = model.resolve()
    solution.set_objective(objective)

    constructive = PostModel(problem, solution)
    constructive.run()

    return constructive


def solve(
    problem: Problem,
    solution: Solution,
    constructive: Constructive, 
    parms: Parmeters
) -> Optional[Heuristic]:
    """This functions runs the selected heuristic approach.

    Args:
        problem (Problem): The problem reference.
        solution (Solution): The solution reference.
        constructive (Constructive): The constructive procedure.
        parms (Parmeters): The operating guidelines.

    Returns:
        Optional[Heuristic]: The heuristic procedure.
    """
    solver: Optional[Heuristic] = None
    if parms['algorithm'] == 'lahc': solver = LAHC(problem, parms['lsize'])
    elif parms['algorithm'] == 'sa': solver = SA(
        problem, parms['alpha'], parms['t0'], parms['samax']
    )
    else: print_usage(parms)

    create_neighborhoods(problem, solver, constructive)
    solver.run(solution, parms['maxiters'])

    return solver


def create_neighborhoods(
    problem: Problem, 
    solver: Heuristic, 
    constructive: Constructive
) -> None:
    """This function creates the neighborhoods for the heuristic.

    Args:
        problem (Problem): The problem reference.
        solver (Heuristic): The heuristic procedure.
        constructive (Constructive): The constructive procedure.
    """
    solver.add_move(Shift(problem, constructive))
    solver.add_move(SimpleSwap(problem, constructive))
    solver.add_move(Swap(problem, constructive))
    solver.add_move(Switch(problem, constructive))
    solver.add_move(SmartShift(problem, constructive))
    solver.add_move(SmartSimpleSwap(problem, constructive))
    solver.add_move(SmartSwap(problem, constructive))
    solver.add_move(SmartSwitch(problem, constructive))


def feedback_approach(
    solution: Solution, 
    model: LinModel,
    solver: Optional[Heuristic],
    constructive: Constructive,
    parms: Parmeters
) -> None:
    """This functions runs the feedback approach.

    Args:
        solution (Solution): The solution reference.
        model (LinModel): The linear model.
        solver (Heuristic): The heuristic procedure.
        constructive (Constructive): The constructive procedure.
        parms (Parmeters): The operating guidelines.
    """
    for _ in range(parms['feedback']):
        model.add_weights('x', list(solution.weights.values()))
        model.add_weights('y', list(solution.inputs.values()))

        objective: Objective = model.resolve()
        solution.set_objective(objective)

        constructive.run()
        if solver != None: solver.run(solution, parms['maxiters'], True)


def read_args(args: List[str], parms: Parmeters) -> None:
    """This function reads the input arguments.

    Args:
        args (List[str]): The terminal argument list.
        parms (Parmeters): The operating guidelines.
    """
    if len(args) < 3: print_usage(parms)

    index: int = 3
    while index < len(args):
        option: str = args[index]
        index += 1

        if option == '-constructive': parms['constructive'] = args[index]
        elif option == '-algorithm': parms['algorithm'] = args[index]
        elif option == '-feedback': parms['feedback'] = int(args[index])
        elif option == '-seed': parms['seed'] = int(args[index])
        elif option == '-maxiters': parms['maxiters'] = int(args[index])

        # LAHC
        elif option == '-lsize': parms['lsize'] = int(args[index])

        # SA
        elif option == '-alpha': parms['alpha'] = float(args[index])
        elif option == '-samax': parms['samax'] = int(args[index])
        elif option == '-t0': parms['t0'] = float(args[index])
        else: print_usage(parms)
        index += 1


def print_usage(parms: Parmeters) -> None:
    """This function prints the program usage.

    Args:
        parms (Parmeters): The operating guidelines.
    """
    usage: str = \
        f'Usage: python3 src/main.py <input> <output> [options]\n' + \
        f'    <input>  : Name of the problem input file.\n' + \
        f'    <output> : Name of the (output) solution file.\n' + \
        f'\nOptions:\n' + \
        f'    -constructive <constructive> : premodel, postmodel (default: {parms["constructive"]}).\n' + \
        f'    -algorithm <algorithm>       : lahc, sa.\n' + \
        f'    -feedback <feedback>         : maximum number of feedback interactions with the model (defaulf: {parms["feedback"]}).\n' + \
        f'    -seed <seed>                 : random seed (default: {parms["seed"]}).\n' + \
        f'    -maxiters <maxiters>         : maximum number of interactions (default: {parms["maxiters"]}).\n' + \
        f'\n    LAHC parameters:\n' + \
        f'        -lsize <lsize> : LAHC list size (default: {parms["lsize"]}).\n' + \
        f'\n    SA parameters:\n' + \
        f'        -alpha <alpha> : cooling rate for the Simulated Annealing (default: {parms["alpha"]}).\n' + \
        f'        -samax <samax> : iterations before updating the temperature for Simulated Annealing (default: {parms["samax"]}).\n' + \
        f'        -t0 <t0>       : initial temperature for the Simulated Annealing (default: {parms["t0"]}). \n' + \
        f'\nExamples:\n' + \
        f'    python3 src/main.py instance_1.json out_1.json\n' + \
        f'    python3 src/main.py instance_1.json out_1.json -constructive premodel -seed 1\n' + \
        f'    python3 src/main.py instance_1.json out_1.json -algorithm sa -alpha 0.98 -samax 1000 -t0 1e5\n'
    
    print(usage)
    sys.exit()


if __name__ == '__main__':
    main()
