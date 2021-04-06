from algorithm.constructive import Constructive
from model.problem import Problem
from model.solution import Solution
from .move import Move
from typing import Optional, List, Tuple
import random


class SmartSwitch(Move):
    """This class represents a SmartSwitch Move. A neighbor in the SmartSwitch 
    Move structure is generated by switching the order of two jobs of a machine
    with the largest total execution time.
    """

    def __init__(
        self: 'SmartSwitch', 
        problem: Problem, 
        constructive: Constructive
    ):
        """Instantiates a new SmartSwitch Move.

        Args:
            problem (Problem): The problem reference.
            constructive (Constructive): The move constructive procedure.
        """

        super().__init__(problem, constructive, 'SmartSwitch')

        self._make_span: List[Tuple[float, int]] = []
        self._engine_id: Optional[int] = None

        self._job_1: Optional[int] = None
        self._job_2: Optional[int] = None        

    def accept(self: 'SmartSwitch') -> None:
        """This method must be called whenever the modification made by 
        this move is accepted. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        super().accept()

    def reject(self: 'SmartSwitch') -> None:
        """This method must be called whenever the modification made by 
        this move are rejected. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        super().reject()

        route: List[Tuple[int, str]] = \
            self._current_solution.routes[self._engine_id - 1]

        route[self._job_1], route[self._job_2] = \
            route[self._job_2], route[self._job_1]

        self._constructive.run(True)

    def do_move(self: 'SmartSwitch', solution: Solution) -> float:
        """This method returns does the move and returns the impact 
        (delta cost) in the solution.
    
        Args:
            solution (Solution): The solution to be modified.

        Returns:
            float: The impact (delta cost) of this move in the solution.
        """

        route: List[Tuple[int, str]] = \
            solution.routes[self._engine_id - 1]

        self._job_1, self._job_2 = [
            tuple(i)[0] for i in random.sample(list(enumerate(route)), 2)
        ]

        route[self._job_1], route[self._job_2] = \
            route[self._job_2], route[self._job_1]

        return super().do_move(solution)

    def gen_move(self: 'SmartSwitch', solution: Solution) -> None:
        """This method generates a random candidate for the movement that must 
        be subsequently validated by has_move ().
        
        Args:
            solution (Solution): The solution to be modified.
        """

        # resets the current neighborhood so that new ones can be explored
        self.reset()

        for _ in range(int(1e3)):
            self._engine_id = random.choice(self._make_span)[1]
            if self.has_move(solution): break

    def has_move(self: 'SmartSwitch', solution: Solution) -> bool:
        """This method returns a boolean indicating whether this neighborhood 
        can be applied to the current solution.
        
        Returns:
            bool: True if this neighborhood can be applied to the current 
                solution, False otherwise.
        """

        return len(solution.routes[self._engine_id - 1]) > 1

    def reset(self: 'SmartSwitch') -> None:
        """This method is called whenever the neighborhood should be reset 
        (mainly to avoid the need of creating another object).
        """

        engine_duration: List[Tuple[float, int]] = [
            (item['duration'], item['engine']) 
            for item in self._current_solution.reclaims
        ]

        self._make_span = filter(
            lambda x: x[0] == max(engine_duration)[0], 
            engine_duration
        )

        self._engine_id = random.choice(self._make_span)[1]
        
        self._job_1 = None
        self._job_2 = None

    # region simple getters and setters
    @property
    def make_span(self: 'SmartSwitch') -> List[Tuple[float, int]]:
        """List[Tuple[float, int]]: List containing a tuple with the makespan 
        and the id of each engine.
        """
        return self._make_span

    @make_span.setter
    def make_span(self: 'SmartSwitch', value: List[Tuple[float, int]]) -> None:
        self.make_span = value

    @property
    def engine_id(self: 'SmartSwitch') -> Optional[int]:
        """Optional[int]: The engine id."""
        return self._engine_id

    @engine_id.setter
    def engine_id(self: 'SmartSwitch', value: Optional[int]) -> None:
        self._engine = value

    @property
    def job_1(self: 'SmartSwitch') -> Optional[int]:
        """Optional[int]: The index of the first job."""
        return self._job_1

    @job_1.setter
    def job_1(self: 'SmartSwitch', value: Optional[int]) -> None:
        self._job_1 = value

    @property
    def job_2(self: 'SmartSwitch') -> Optional[int]:
        """Optional[int]: The index of the second job."""
        return self._job_2

    @job_2.setter
    def job_2(self: 'SmartSwitch', value: Optional[int]) -> None:
        self._job_2 = value
