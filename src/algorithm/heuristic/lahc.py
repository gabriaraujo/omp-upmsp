from algorithm.neighborhood import Move
from model.problem import Problem
from model.solution import Solution
from .heuristic import Heuristic
from typing import List
import copy

class LAHC(Heuristic):
    """This class is a Late Acceptance Hill-Climbing implementation."""
    
    def __init__(
        self: 'LAHC', 
        problem: Problem,
        size: int,
    ):
        """Instantiates a new Late Acceptance Hill-Climbing.

        Args:
            problem (Problem): The problem reference.
            size: The number os most recent solutions
        """

        super().__init__(problem, 'Late Acceptance Hill-Climbing')

        self.__size: int = size

    def run(
        self: 'LAHC', 
        initial_solution: Solution,
        max_iters: int,
        best_known: bool = False
    ) -> None:
        """Executes the Late Acceptance Hill-Climbing and updates the best 
        solution. 

        Args:
            initial_solution (Solution): The initial (input) solution.
            max_iters (int): The maximum number of iterations to execute.
            best_known (bool): True if the initial best_solution have already 
                been established, False otherwise. Note that the False option 
                will define the initial best_solution as the initial_solution. 
                Defaults to False.
        """

        # list of costs for each solution
        cost_list: List[float] = [
            initial_solution.cost * 1.5 for _ in range(self.__size)
        ]

        if not best_known:
            self._best_solution = initial_solution

        solution: Solution = copy.deepcopy(initial_solution)

        # cost list index
        v: int = 0

        for _ in range(max_iters):
            move: Move = self.select_move(solution)
            move.do_move(solution)

            if (solution.cost <= move.initial_cost or 
                solution.cost <= cost_list[v]):
                self.accept_move(move)

                if solution.cost < self._best_solution.cost:
                    self._best_solution = copy.deepcopy(solution)

            else:
                self.reject_move(move)

            cost_list[v] = solution.cost
            v = (v + 1) % self.__size

    # region simple getters and setters
    @property
    def size(self: 'LAHC') -> int:
        """ int: The number os most recent solutions."""
        return self.__size

    @size.setter
    def size(self: 'LAHC', value: int) -> None:
        self.__size = value
