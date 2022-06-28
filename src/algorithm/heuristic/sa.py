from algorithm.neighborhood import Move
from model.problem import Problem
from model.solution import Solution
from .heuristic import Heuristic
import random
import math
import copy

class SA(Heuristic):
    """This class is a Simulated Annealing implementation."""
    
    def __init__(
        self: 'SA', 
        problem: Problem,
        alpha: float,
        t0: float,
        sa_max: int = int(1e3)
    ):
        """Instantiates a new Simulated Annealing.

        Args:
            problem (Problem): The problem reference.
            alpha (float): Cooling rate for the simulated annealing.
            t0 (float): Initial temperature.
            sa_max (int): Number of iterations before update the temperature. 
                Defaults to 1e4.
        """

        super().__init__(problem, 'Simulated Annealing')

        self.__alpha: float = alpha
        self.__t0: float = t0
        self.__sa_max: int = sa_max
        
        self.__eps: float = 1e-6

    def run(
        self: 'SA', 
        initial_solution: Solution,
        max_iters: int,
        best_known: bool = False
    ) -> None:
        """Executes the Simulated Annealing and updates the best solution. 

        Args:
            initial_solution (Solution): The initial (input) solution.
            max_iters (int): The maximum number of iterations to execute.
            best_known (bool): True if the initial best_solution have already 
                been established, False otherwise. Note that the False option 
                will define the initial best_solution as the initial_solution. 
                Defaults to False.
        """

        if not best_known:
            self._best_solution = initial_solution

        solution: Solution = copy.deepcopy(initial_solution)
        temperature: float = self.__t0
        
        self._iters = 0
        while temperature > self.__eps and self._iters < max_iters:
            for _ in range(self.__sa_max):
                solution.start_time = initial_solution.start_time.copy()

                move: Move = self.select_move(solution)
                delta: float = move.do_move(solution)

                # if the solution is improved
                if delta < 0:
                    self.accept_move(move)
                    # self._iters = 0

                    if (solution.cost < self._best_solution.cost):
                        self._best_solution = copy.deepcopy(solution)

                # if solution is not improved, but is accepted
                elif delta == 0:
                    self.accept_move(move)

                # solution is not improved, but may be accepted with a probability
                else:
                    x: float = random.uniform(0, 1)
                    if x < math.exp(-delta / temperature):
                        self.accept_move(move)

                    # if solution is rejected
                    else:
                        self.reject_move(move)

            self._iters += 1
            temperature *= self.__alpha

            # if necessary, updates temperature
            if temperature < self.__eps:
                temperature = self.__t0

    # region simple getters and setters
    @property
    def alpha(self: 'SA') -> float:
        """float: Cooling rate for the simulated annealing."""
        return self.__alpha

    @alpha.setter
    def alpha(self: 'SA', value: float) -> None:
        self.__alpha = value

    @property
    def t0(self: 'SA') -> float:
        """float: Initial temperature."""
        return self.__t0

    @t0.setter
    def t0(self: 'SA', value: float) -> None:
        self.__t0 = value

    @property
    def sa_max(self: 'SA') -> int:
        """int: The maximum number of iterations without improvements to 
        execute.
        """
        return self.__sa_max

    @sa_max.setter
    def sa_max(self:'SA', value: int) -> None:
        self.__sa_max = value

    @property
    def eps(self: 'SA') -> float:
        """float: Conceptual zero (mainly to avoid zero division error)."""
        return self.__eps

    @eps.setter
    def eps(self: 'SA', value: float) -> None:
        self.__eps = value

