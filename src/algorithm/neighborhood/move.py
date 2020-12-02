from algorithm.constructive import Constructive
from model.problem import Problem
from model.solution import Solution
from typing import Optional

class Move:
    """This class represents a Move (or Neighborhood). The basic methods as 
    well as several counters (for future analysis) are included.
    """

    def __init__(
        self: 'Move', 
        problem: Problem, 
        constructive: Constructive, 
        name: str
    ):
        """Instantiates a new Move.

        Args:
            problem (Problem): The problem reference.
            constructive (Constructive): The move constructive procedure.
            name (str): The name of this neighborhood (for debugging purposes).
        """

        self._problem: Problem = problem
        self._name: str = name

        self._constructive: Constructive = constructive

        self._current_solution: Optional[Solution] = None
        self._intermediate_state: bool = False

        self._delta_cost: float = 0.0
        self._initial_cost: float = float('inf')

        # basic statistics for future analysis
        self.__iters: int = 0
        self.__improvements: int = 0
        self.__sideways: int = 0
        self.__worsens: int = 0
        self.__rejects: int = 0

    def accept(self: 'Move') -> None:
        """This method must be called whenever the modification made by 
        this move is accepted. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        assert self._intermediate_state, \
            'calling accept() before calling do_move().'

        self._intermediate_state = False

        # updating counters
        if self._delta_cost < 0:
            self.__improvements += 1
        elif self._delta_cost == 0:
            self.__sideways += 1
        else:
            self.__worsens += 1

    def reject(self: 'Move') -> None:
        """This method must be called whenever the modification made by 
        this move are rejected. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        assert self._intermediate_state, \
            'calling reject() before calling do_move().'

        self._intermediate_state = False

        # updating counters
        self.__rejects += 1

    def do_move(self: 'Move', solution: Solution) -> float:
        """This method returns does the move and returns the impact 
        (delta cost) in the solution.
    
        Args:
            solution (Solution): The solution to be modified.

        Returns:
            float: The impact (delta cost) of this move in the solution.
        """

        assert self.has_move(solution), \
            f'move {self._name} being executed with has_move() = False.'
        assert not self._intermediate_state, \
            'calling do_move() before mandatory call to accept() or reject().'

        self._intermediate_state = True

        self.__iters += 1
        self._current_solution = solution
        self._initial_cost = solution.cost

        self._constructive.solution = solution
        self._constructive.run(True)

        self._delta_cost = solution.cost - self._initial_cost
        return self._delta_cost

    def gen_move(self: 'Move', solution: Solution) -> None:
        """This method generates a random candidate for the movement that must 
        be subsequently validated by has_move ().
        
        Args:
            solution (Solution): The solution to be modified.
        """

        raise NotImplementedError

    def has_move(self: 'Move', solution: Solution) -> bool:
        """This method returns a boolean indicating whether this neighborhood 
        can be applied to the current solution.

        Args:
            solution (Solution): The solution to be evaluated.
     
        Returns:
            bool: True if this neighborhood can be applied to the current 
                solution, False otherwise.
        """

        raise NotImplementedError

    def reset(self: 'Move') -> None:
        """This method is called whenever the neighborhood should be reset 
        (mainly to avoid the need of creating another object).
        """

        raise NotImplementedError

    # region simple getters and setters
    @property
    def problem(self: 'Move') -> Problem:
        """Problem: The problem reference."""
        return self._problem

    @problem.setter
    def problem(self: 'Move', value: Problem) -> None:
        self._problem = value

    @property
    def constructive(self: 'Move') -> Constructive:
        """Constructive: The move constructive procedure."""
        return self._constructive

    @constructive.setter
    def constructive(self: 'Move', value: Constructive) -> None:
        self._constructive = value

    @property
    def name(self: 'Move') -> str:
        """str: The move name."""
        return self._name

    @name.setter
    def name(self: 'Move', value: str) -> None:
        self._name = value

    @property
    def current_solution(self: 'Move') -> Solution:
        """Solution: The current solution reference."""
        return self._current_solution

    @current_solution.setter
    def current_solution(self: 'Move', value: Solution) -> None:
        self._current_solution = value

    @property
    def intermediate_state(self: 'Move') -> bool:
        """bool: flag to indicate whether the movement is in the intermediate 
        state.
        """
        return self._intermediate_state

    @intermediate_state.setter
    def intermediate_state(self: 'Move', value: bool) -> None:
        self._intermediate_state = value

    @property
    def delta_cost(self: 'Move') -> float:
        """float: The move delta cost."""
        return self._delta_cost

    @delta_cost.setter
    def delta_cost(self: 'Move', value: float) -> None:
        self._delta_cost = value

    @property
    def initial_cost(self: 'Move') -> float:
        """float: The move initial cost."""
        return self._initial_cost

    @initial_cost.setter
    def initial_cost(self: 'Move', value: float) -> None:
        self._initial_cost = value

    @property
    def iters(self: 'Move') -> int:
        """int: The move interaction counter."""
        return self.__iters

    @iters.setter
    def iters(self: 'Move', value: int) -> None:
        self.__iters = value

    @property
    def improvements(self: 'Move') -> int:
        """int: The move improvements counter."""
        return self.__improvements

    @improvements.setter
    def improvements(self: 'Move', value: int) -> None:
        self.__improvements = value

    @property
    def sideways(self: 'Move') -> int:
        """float: the move sideways counter."""
        return self.__sideways

    @sideways.setter
    def sideways(self: 'Move', value: int) -> None:
        self.__sideways = value

    @property
    def worsens(self: 'Move') -> int:
        """int: The move worsens counter."""
        return self.__worsens

    @worsens.setter
    def worsens(self: 'Move', value: int) -> None:
        self.__worsens = value

    @property
    def rejects(self: 'Move') -> int:
        """int: the move rejects counter."""
        return self.__rejects

    @rejects.setter
    def rejects(self: 'Move', value: int) -> None:
        self.__rejects = value
