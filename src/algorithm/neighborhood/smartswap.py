from algorithm.constructive import Constructive
from model.problem import Problem
from model.solution import Solution
from .move import Move
from typing import Optional, List, Tuple
import random


class SmartSwap(Move):
    """This class represents a SmartSwap Move. A neighbor in the SmartSwap 
    Neighborhood is generated by swapping two jobs between two machines, with 
    at least one of these machines has the largest total execution time. Note 
    that the swapped jobs may be placed in any position on the other machine, 
    i.e. the original positions are not taken into account. This Move first 
    removes the two jobs and then reinserts them in random positions.
    """

    def __init__(
        self: 'SmartSwap', 
        problem: Problem, 
        constructive: Constructive
    ):
        """Instantiates a new SmartSwap Move.

        Args:
            problem (Problem): The problem reference.
            constructive (Constructive): The move constructive procedure.
        """

        super().__init__(problem, constructive, 'SmartSwap')

        self._make_span: List[Tuple[float, int]] = []
        self._engine_1_id: Optional[int] = None
        self._engine_2_id: Optional[int] = None

        self._route_1: List[Tuple[int, str]] = []
        self._route_2: List[Tuple[int, str]] = []

        self._job_1: Tuple[int, str] = ()
        self._job_2: Tuple[int, str] = ()

        self._pos_1: Optional[int] = None
        self._pos_2: Optional[int] = None

    def accept(self: 'SmartSwap') -> None:
        """This method must be called whenever the modification made by 
        this move is accepted. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        super().accept()

    def reject(self: 'SmartSwap') -> None:
        """This method must be called whenever the modification made by 
        this move are rejected. It ensures that the solution as well as 
        other structures are updated accordingly.
        """

        super().reject()

        self._route_1.remove(self._job_2)
        self._route_2.remove(self._job_1)

        self._route_1.insert(self._pos_1, self._job_1)
        self._route_2.insert(self._pos_2, self._job_2)

        self._constructive.run(True)

    def do_move(self: 'SmartSwap', solution: Solution) -> float:
        """This method returns does the move and returns the impact 
        (delta cost) in the solution.
    
        Args:
            solution (Solution): The solution to be modified.

        Returns:
            float: The impact (delta cost) of this move in the solution.
        """

        self._pos_1 = self._route_1.index(self._job_1)
        self._pos_2 = self._route_2.index(self._job_2)

        self._route_1.remove(self._job_1)
        self._route_2.remove(self._job_2)

        try:
            self._route_1.insert(random.randrange(len(self._route_1)), self._job_2)
            self._route_2.insert(random.randrange(len(self._route_2)), self._job_1)

        except ValueError:
            self._route_1.insert(self._pos_1, self._job_2)
            self._route_2.insert(self._pos_2, self._job_1)

        return super().do_move(solution)

    def gen_move(self: 'SmartSwap', solution: Solution) -> None:
        """This method generates a random candidate for the movement that must 
        be subsequently validated by has_move().
        
        Args:
            solution (Solution): The solution to be modified.
        """

        self._current_solution = solution

        # resets the current neighborhood so that new ones can be explored
        self.reset()

        for _ in range(int(1e3)):
            self._job_1 = random.choice(self._route_1)
            self._job_2 = random.choice(self._route_2)
            if self.has_move(solution): break

    def has_move(self: 'SmartSwap', solution: Solution) -> bool:
        """This method returns a boolean indicating whether this neighborhood 
        can be applied to the current solution.

        Args:
            solution (Solution): The solution to be evaluated.
        
        Returns:
            bool: True if this neighborhood can be applied to the current 
                solution, False otherwise.
        """

        return self._job_1[1] == self._job_2[1]

    def reset(self: 'SmartSwap') -> None:
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

        self._engine_1_id = random.choice(self._make_span)[1]

        # try to get the engine from the neighboring yard
        try:
            self._engine_2_id = self._problem.engines[self._engine_1_id]

        except IndexError:
            self._engine_2_id = self._problem.engines[self._engine_1_id - 2]

        self._route_1 = self._current_solution.routes[self._engine_1_id - 1]
        self._route_2 = self._current_solution.routes[self._engine_2_id - 1]

        self._job_1 = random.choice(self._route_1)
        self._job_2 = random.choice(self._route_2)

        self._pos_1 = self._route_1.index(self._job_1)
        self._pos_2 = self._route_2.index(self._job_2)

    # region simple getters and setters
    @property
    def make_span(self: 'SmartSwap') -> List[Tuple[float, int]]:
        """List[Tuple[float, int]]: List containing a tuple with the makespan 
        and the id of each engine.
        """
        return self._make_span

    @make_span.setter
    def make_span(self: 'SmartSwap', value: List[Tuple[float, int]]) -> None:
        self.make_span = value

    @property
    def engine_1_id(self: 'SmartSwap') -> Optional[int]:
        """Optional[int]: The first engine id."""
        return self._engine_1_id

    @engine_1_id.setter
    def engine_1_id(self: 'SmartSwap', value: Optional[int]) -> None:
        self._engine_1_id = value

    @property
    def engine_2_id(self: 'SmartSwap') -> Optional[int]:
        """Optional[int]: The second engine id."""
        return self._engine_2_id

    @engine_2_id.setter
    def engine_2_id(self: 'SmartSwap', value: Optional[int]) -> None:
        self._engine_2_id = value

    @property
    def route_1(self: 'SmartSwap') -> List[Tuple[int, str]]:
        """List[Tuple[int, str]]: The route of the first engine."""
        return self._route_1

    @route_1.setter
    def route_1(self: 'SmartSwap', value: List[Tuple[int, str]]) -> None:
        self._route_1 = value

    @property
    def route_2(self: 'SmartSwap') -> List[Tuple[int, str]]:
        """List[Tuple[int, str]]: The route of the second engine."""
        return self._route_2

    @route_2.setter
    def route_2(self: 'SmartSwap', value: List[Tuple[int, str]]) -> None:
        self._route_2 = value

    @property
    def job_1(self: 'SmartSwap') -> Tuple[int, str]:
        """Tuple[int, str]: The selected job from the first engine route."""
        return self._job_1

    @job_1.setter
    def job_1(self: 'SmartSwap', value: Tuple[int, str]) -> None:
        self._job_1 = value

    @property
    def job_2(self: 'SmartSwap') -> Tuple[int, str]:
        """Tuple[int, str]: The selected job from the second engine route."""
        return self._job_2

    @job_2.setter
    def job_2(self: 'SmartSwap', value: Tuple[int, str]) -> None:
        self._job_2 = value

    @property
    def pos_1(self: 'SmartSwap') -> Optional[int]:
        """Optional[int]: The index of the first job."""
        return self._pos_1

    @pos_1.setter
    def pos_1(self: 'SmartSwap', value: Optional[int]) -> None:
        self._pos_1 = value

    @property
    def pos_2(self: 'SmartSwap') -> Optional[int]:
        """Optional[int]: The index of the second job."""
        return self._pos_2

    @pos_2.setter
    def pos_2(self: 'SmartSwap', value: Optional[int]) -> None:
        self._pos_2 = value