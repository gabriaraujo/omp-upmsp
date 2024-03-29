from algorithm.constructive import Constructive
from model.problem import Problem
from model.solution import Solution
from .move import Move
from typing import Optional, List, Tuple
import random

class SmartShift(Move):
    """This class represents a Smart Shift Move. A neighbor in the Smart Shift 
    Move is generated by re-scheduling one job from a machine with the largest 
    total execution time to another position in the machine.
    """

    def __init__(
        self: 'SmartShift', 
        problem: Problem, 
        constructive: Constructive
    ):
        """Instantiates a new SmartShift Move.

        Args:
            problem (Problem): The problem reference.
            constructive (Constructive): The move constructive procedure.
        """
        super().__init__(problem, constructive, 'SmartShift')

        self._make_span: List[Tuple[float, int]] = []
        self._engine_id: Optional[int] = None
        self._route: List[Tuple[int, str]] = []
        self._job: Tuple[int, str] = ()
        self._pos: Optional[int] = None

    def accept(self: 'SmartShift') -> None:
        """This method must be called whenever the modification made by 
        this move is accepted. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        super().accept()

    def reject(self: 'SmartShift') -> None:
        """This method must be called whenever the modification made by 
        this move are rejected. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        super().reject()

        self._route.remove(self._job)
        self._route.insert(self._pos, self._job)

        self._constructive.run(True)

    def do_move(self: 'SmartShift', solution: Solution) -> float:
        """This method returns does the move and returns the impact 
        (delta cost) in the solution.
    
        Args:
            solution (Solution): The solution to be modified.

        Returns:
            float: The impact (delta cost) of this move in the solution.
        """

        self._job = random.choice(self._route)
        self._pos = self._route.index(self._job)

        self._route.remove(self._job)
        self._route.insert(random.randrange(len(self._route)), self._job)

        return super().do_move(solution)

    def gen_move(self: 'SmartShift', solution: Solution) -> None:
        """This method generates a random candidate for the movement that must 
        be subsequently validated by has_move().
        
        Args:
            solution (Solution): The solution to be modified.
        """

        self._current_solution = solution

        # resets the current neighborhood so that new ones can be explored
        self.reset()

        for _ in range(int(1e3)):
            self._engine_id = random.choice(self._make_span)[1]
            self._route = self._current_solution.routes[self._engine_id - 1]
            if self.has_move(solution): break

    def has_move(self: 'SmartShift', solution: Solution) -> bool:
        """This method returns a boolean indicating whether this neighborhood 
        can be applied to the current solution.

        Args:
            solution (Solution): The solution to be evaluated.
        
        Returns:
            bool: True if this neighborhood can be applied to the current 
                solution, False otherwise.
        """

        return len(self._route) > 1

    def reset(self: 'SmartShift') -> None:
        """This method is called whenever the neighborhood should be reset 
        (mainly to avoid the need of creating another object).
        """

        engine_duration: List[Tuple[float, int]] = [
            (item['duration'], item['engine']) 
            for item in self._current_solution.reclaims
        ]

        self._make_span = list(filter(
            lambda x: x[0] == max(engine_duration)[0], 
            engine_duration
        ))

        self._engine_id = random.choice(self._make_span)[1]
        self._route = self._current_solution.routes[self._engine_id - 1]
        self._job = random.choice(self._route)
        self._pos = self._route.index(self._job)

    # region simple getters and setters
    @property
    def make_span(self: 'SmartShift') -> List[Tuple[float, int]]:
        """List[Tuple[float, int]]: List containing a tuple with the makespan 
        and the id of each engine.
        """
        return self._make_span

    @make_span.setter
    def make_span(self: 'SmartShift', value: List[Tuple[float, int]]) -> None:
        self.make_span = value

    @property
    def engine_id(self: 'SmartShift') -> Optional[int]:
        """Optional[int]: The engine id."""
        return self._engine_id

    @engine_id.setter
    def engine_id(self: 'SmartShift', value: Optional[int]) -> None:
        self._engine = value

    @property
    def route(self: 'SmartShift') -> List[Tuple[int, str]]:
        """List[Tuple[int, str]]: The route of the engine."""
        return self._route

    @route.setter
    def route(self: 'SmartShift', value: List[Tuple[int, str]]) -> None:
        self._route_1 = value

    @property
    def job(self: 'SmartShift') -> Tuple[int, str]:
        """Tuple[int, str]: The selected job from the engine route."""
        return self._job

    @job.setter
    def job(self: 'SmartShift', value: Tuple[int, str]) -> None:
        self._job = value

    @property
    def pos(self: 'SmartShift') -> Optional[int]:
        """Optional[int]: The index of the job."""
        return self._pos

    @pos.setter
    def pos(self: 'SmartShift', value: Optional[int]) -> None:
        self._pos = value