from config import Route
from model.classes import Engine
from model.problem import Problem
from model.solution import Solution
from typing import List, Optional


class Constructive:
    """This class contains simple constructive procedures for the Machine
    Scheduling Problem. Generates and returns a greedy solution. The jobs are 
    added in a specific order to the machine to which they incur the smallest 
    increase in the makespan.
    """

    def __init__(
        self: 'Constructive', 
        problem: Problem, 
        solution: Solution
    ):
        """Instantiates a new Constructive for the Machine Scheduling Problem.

        Args:
            problem (Problem): The problem reference.
            solution (Solution): The OMP solution reference.
        """

        self._problem: Problem = problem
        self._solution: Solution = solution
        
        self._output_id: Optional[int] = None
        self._weights: List[List[float]] = list(solution.weights.values()) 
        self._inputs: List[float] = [
            sum(inp) for inp in list(solution.inputs.values())
        ]

    def run(self: 'Constructive', has_routes: bool = False) -> None:
        """Executes the Constructive for all output requests.
        
        Args:
            has_routes (bool): Flag to indicate if the routes are already 
                defined. True if the routes have already been established, 
                False otherwise. Note that the False option will define the 
                routes automatically and greedily. Defaults to False.
        """

        # resets the solution start time for each execution
        self._solution._start_time = [0] * len(self._problem.engines)

        # the output_id must have already been specified for the defined route
        if has_routes:
            self.build()

        else:
            for out in self._problem.outputs:
                self._output_id = out.id - 1
                self.set_routes()
                self.build()

        self.reset_inputs()

    def build(self: 'Constructive') -> None:
        """This method defines the operations performed on each stockpile and 
        their durations.
        
        To use this method outside the run() method, you must manually assign 
        the value of the output_id attribute of the Constructive class 
        and the routes attribute of the Solution class before using it.
        """

        assert self._solution.weights, \
            'calling build() with an empty list of weights.'

        assert self._solution.inputs, \
            'calling build() with an empty list of inputs.'

        assert self._output_id >= 0, \
            'calling build() before specifying the output request ID.'

        assert self._solution.routes != [], \
            'calling build() before defining the routes for each machine.'

        # reset the solution to save new results
        self._solution.reset()
 
        for eng, route, in zip(self._problem.engines, self._solution.routes):
            for stp, atv in route:
                
                # setup time, if there is more than one job in the same stockpile
                setup_time: float = 0.0

                # reclaimery time
                duration: float = round(
                    self._weights[self._output_id][stp] / eng.speed_reclaim, 2
                ) if eng.speed_reclaim > 0 else 0

                # travel time and setup to stockpile
                time_travel: float = self._problem.time_travel[eng.pos_ini][stp]

                # performs the stacking activity before performing the reclaiming
                if atv == 's' or atv == 'b':
                    self._solution.stacks.append({
                        'weight': round(self._inputs[stp], 1),
                        'stockpile': stp + 1,
                        'engine': eng.id,
                        'start_time': round(
                            self._solution.start_time[eng.id - 1] + time_travel, 
                            2
                        ),
                        'duration': round(
                            self._inputs[stp] / eng.speed_stack, 2
                        ),
                    })

                    # adds stacking time if there is any input
                    self._solution.start_time[eng.id - 1] += \
                        self._solution.stacks[-1]['duration']
                    setup_time += self._problem.time_travel[stp][stp]
                    self._inputs[stp] = 0.0

                # ore reclaim activity from the stockpile
                if atv == 'r' or atv == 'b':
                    self._solution.reclaims.append({
                        'weight': round(self._weights[self._output_id][stp], 1),
                        'stockpile': stp + 1,
                        'engine': eng.id,
                        'start_time': round(
                            self._solution.start_time[eng.id - 1] 
                                + time_travel + setup_time, 
                            2
                        ),
                        'duration': duration,
                        'output': self._output_id + 1
                    })

                self._solution.start_time[eng.id - 1] += duration + time_travel

            # changes the starting position of the machine
            try:
                eng.pos_ini = route[-1][0]

            # if the machine has not received any jobs
            except IndexError:
                pass

        # updates the cost
        self._solution.update_cost(self._output_id + 1)

    def set_routes(self: 'Constructive') -> None:
        """This method defines the order of operation of all machines and save 
        the result in the routes attribute of the Solution class.
        """

        routes: List[Route] = []
        start_time: List[float] = self._solution.start_time.copy()

        # appends the individual machine's route to the route list
        for engine in self._problem.engines:
            routes.append(self.set_route(start_time, engine))

        self.set_jobs(routes)

    def set_route(
        self: 'Constructive',
        start_time: List[float],
        engine: Engine
    ) -> Route:
        """This method greedily defines the operating order of each individual 
        machine. It assigns all possible jobs to each machine, which must be 
        further refined by set_jobs().

        Args:
            start_time (List[float]): List with the time when each engine can 
                start a new task.
            engine (Engine): The engine reference.

        Returns:
            List[Tuple[float, int, int, str]]: List of tuples whose first  
                element is the access time of the machine to the stockpile, 
                the second element is the engine ID, the third element is its 
                position and the last element is its configuration.
        """

        raise NotImplementedError

    def set_jobs(self: 'Constructive', routes: List[Route]) -> None:
        """This method defines greedily where each machine will act based on 
        its routes and the start time of each job.
        """

        raise NotImplementedError

    def reset_inputs(self: 'Constructive') -> None:
        """This method is called whenever the input list should be reset 
        (mainly to avoid the need of creating another object).
        """
        
        self._inputs = [
            sum(inp) for inp in list(self._solution.inputs.values())
        ]

    # region simple getters and setters
    @property
    def problem(self: 'Constructive') -> Problem:
        """Problem: The problem considered."""
        return self._problem

    @problem.setter
    def problem(self: 'Constructive', value: Problem) -> None:
        self._problem = value

    @property
    def solution(self: 'Constructive') -> Solution:
        """Solution: The solution reference."""
        return self._solution

    @solution.setter
    def solution(self: 'Constructive', value: Solution) -> None:
        self._solution = value

    @property
    def output_id(self: 'Constructive') -> Optional[int]:
        """Optional[int]: The output request identifier."""
        return self._output_id

    @output_id.setter
    def output_id(self: 'Constructive', value: Optional[int]) -> None:
        self._output_id = value

    @property
    def weights(self: 'Constructive') -> List[List[float]]:
        """List[List[float]]: List of lists with the weights retrieved from 
        each output request, in which the lines are the requests and the 
        columns, the stockpiles.
        """
        return self._weights

    @weights.setter
    def weights(self: 'Constructive', value: List[List[float]]) -> None:
        self._weights = value

    @property
    def inputs(self: 'Constructive') -> List[float]:
        """List[float]: List with the stacked weights, in which the columns are 
        the stockpiles.
        """
        return self._inputs

    @inputs.setter
    def inputs(self: 'Constructive', value: List[float]) -> None:
        self._inputs = value
