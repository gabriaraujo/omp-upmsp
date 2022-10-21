from algorithm.constructive import Constructive
from model.classes import Engine
from model.problem import Problem
from model.solution import Solution
from .move import Move
from typing import Optional, List, Tuple
import random

class Shift(Move):
    """This class represents a Shift Move. A neighbor in the Shift Move is 
    generated by re-scheduling one job from a random machine to another 
    position in the machine.
    """
    
    def __init__(
        self: 'Shift', 
        problem: Problem, 
        constructive: Constructive
    ):
        """Instantiates a new Shift Move.

        Args:
            problem (Problem): The problem reference.
            constructive (Constructive): The move constructive procedure.
        """
        super().__init__(problem, constructive, 'Shift')

        self._engine: Engine = random.choice(problem.engines)
        self._route: List[Tuple[int, str]] = []
        self._job: Tuple[int, str] = ()
        self._pos: Optional[int] = None

    def accept(self: 'Shift') -> None:
        """This method must be called whenever the modification made by 
        this move is accepted. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        super().accept()

    def reject(self: 'Shift') -> None:
        """This method must be called whenever the modification made by 
        this move are rejected. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        super().reject()

        self._route.remove(self._job)
        self._route.insert(self._pos, self._job)

        self._constructive.run(True)

    def do_move(self: 'Shift', solution: Solution) -> float:
        """This method returns does the move and returns the impact 
        (delta cost) in the solution.
    
        Args:
            solution (Solution): The solution to be modified.

        Returns:
            float: The impact (delta cost) of this move in the solution.
        """
        if self.has_move(solution):
            self._job = random.choice(self._route)
            self._pos = self._route.index(self._job)

            self._route.remove(self._job)
            self._route.insert(random.randrange(len(self._route)), self._job)

        return super().do_move(solution)

    def gen_move(self: 'Shift', solution: Solution) -> None:
        """This method generates a random candidate for the movement that must 
        be subsequently validated by has_move().
        
        Args:
            solution (Solution): The solution to be modified.
        """

        self._current_solution = solution

        # resets the current neighborhood so that new ones can be explored
        self.reset()

        for _ in range(int(1e3)):
            self._engine = random.choice(self._problem.engines)
            self._route = self._current_solution.routes[self._engine.id - 1]
            if self.has_move(solution): break

    def has_move(self: 'Shift', solution: Solution) -> bool:
        """This method returns a boolean indicating whether this neighborhood 
        can be applied to the current solution.

        Args:
            solution (Solution): The solution to be evaluated.
        
        Returns:
            bool: True if this neighborhood can be applied to the current 
                solution, False otherwise.
        """

        return len(self._route) > 1

    def reset(self: 'Shift') -> None:
        """This method is called whenever the neighborhood should be reset 
        (mainly to avoid the need of creating another object).
        """

        self._engine = random.choice(self._problem.engines)
        self._route = self._current_solution.routes[self._engine.id - 1]
        self._job = random.choice(self._route)
        self._pos = self._route.index(self._job)

    # region simple getters and setters
    @property
    def engine(self: 'Shift') -> Engine:
        """Engine: The engine reference."""
        return self._engine

    @engine.setter
    def engine(self: 'Shift', value: Engine) -> None:
        self._engine = value

    @property
    def route(self: 'Shift') -> List[Tuple[int, str]]:
        """List[Tuple[int, str]]: The route of the engine."""
        return self._route

    @route.setter
    def route(self: 'Shift', value: List[Tuple[int, str]]) -> None:
        self._route = value

    @property
    def job(self: 'Shift') -> Tuple[int, str]:
        """Tuple[int, str]: The selected job from the engine route."""
        return self._job

    @job.setter
    def job(self: 'Shift', value: Tuple[int, str]) -> None:
        self._job = value

    @property
    def pos(self: 'Shift') -> Optional[int]:
        """Optional[int]: The index of the job."""
        return self._pos

    @pos.setter
    def pos(self: 'Shift', value: Optional[int]) -> None:
        self._pos = value