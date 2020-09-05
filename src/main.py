from config import Objective
from algorithm.constructive import LinModel, SimpleConstructive
from algorithm.neighborhood import Move, Swap, Switch
from algorithm.heuristic import SA
from model.problem import Problem
from model.solution import Solution
import random
import sys


def main():
    random.seed(sys.argv[3])

    problem: Problem = Problem('./tests/' + sys.argv[1])
    solution: Solution = Solution(problem)

    model: LinModel = LinModel(problem)
    objective: Objective = model.resolve()
    solution.set_objective(objective)

    constructive: SimpleConstructive = SimpleConstructive(problem, solution)
    constructive.run()

    solver: SA = SA(problem, 0.99, 1.0)

    # solver.add_move(Swap(problem, constructive))
    solver.add_move(Switch(problem, constructive))

    for out in problem.outputs:
        constructive.output_id = out.id - 1
        solver.run(solution, 300, 1e4)

    solver.best_solution.set_deliveries()
    solver.best_solution.write('./out/json/' + sys.argv[2])


if __name__ == '__main__':
    main()
