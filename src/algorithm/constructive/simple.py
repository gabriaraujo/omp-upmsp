from config import Route
from model.classes import Engine
from model.problem import Problem
from model.solution import Solution
from heapq import heapify, heappop
from typing import List, Optional


class SimpleConstructive:
    """This class contains simple constructive procedures for the Machine
    Scheduling Problem. Generates and returns a greedy solution. The jobs are 
    added in a specific order to the machine to which they incur the smallest 
    increase in the makespan.
    """

    def __init__(
        self: 'SimpleConstructive', 
        problem: Problem, 
        solution: Solution
    ):
        """Instantiate a new Constructive for the Machine Scheduling Problem.

        Args:
            problem (Problem): The problem reference.
            solution (Solution): The OMP solution reference.
        """

        assert solution.weights, \
            'trying to instantiate the class with an empty list of weights.'

        assert solution.inputs, \
            'trying to instantiate the class with an empty list of inputs.'

        self._problem: Problem = problem
        self._solution: Solution = solution
        
        self._output_id: Optional[int] = None
        self._weights: List[List[float]] = list(solution.weights.values()) 
        self._inputs: List[float] = [
            sum(inp) for inp in list(solution.inputs.values())
        ]

    def run(self: 'SimpleConstructive', has_routes: bool = False) -> None:
        """Executes the Constructive for all output requests.
        
        Args:
            has_routes (bool): Flag to indicate if the routes are already 
                defined. True if the routes have already been established, 
                False otherwise. Note that the False option will define the 
                routes automatically and greedily. Defaults to False.
        """

        # the output_id must have already been specified for the defined route
        if has_routes:
            self.set_jobs()

        else:
            for out in self._problem.outputs:
                self._output_id = out.id - 1
                self.__set_routes()
                self.set_jobs()

        self.__reset_inputs()

    def set_jobs(self: 'SimpleConstructive') -> None:
        """This method defines the operations performed on each stockpile and 
        their durations.
        
        To use this method outside the run() method, you must manually assign 
        the value of the output_id attribute of the SimpleConstructive class 
        and the routes attribute of the Solution class before using it.
        """

        assert self._output_id >= 0, \
            'calling set_jobs() before specifying the output request ID.'

        assert self._solution.routes != [], \
            'calling set_jobs() before defining the routes for each machine.'

        # reset the solution to save new results
        self._solution.reset()
 
        for eng, route, in zip(self._problem.engines, self._solution.routes):
            for stp, atv in route:
                
                # setup time, if there is more than one job in the same stockpile
                setup_time: float = 0.0

                # reclaimery time
                duration: float = round(
                    self._weights[self._output_id][stp] / eng.speed_reclaim, 1
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
                            1
                        ),
                        'duration': round(
                            self._inputs[stp] / eng.speed_stack, 1
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
                            1
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

    def __set_routes(self: 'SimpleConstructive') -> None:
        """This method defines the order of operation of all machines and save 
        the result in the routes attribute of the Solution class.
        """

        routes: List[Route] = []
        start_time: List[float] = self._solution.start_time.copy()

        # appends the individual machine's route to the route list
        for engine in self._problem.engines:
            routes.append(self.__set_route(start_time, engine))

        self.__set_engines(routes)

    def __set_engines(self: 'SimpleConstructive', routes: List[Route]) -> None:
        """This method defines greedily where each machine will act based on 
        its routes and the start time of each job.
        """

        routes: Route = [item for sublist in routes for item in sublist]
        heapify(routes)

        jobs: List[str] = [''] * len(self._problem.stockpiles)

        while routes:
            route = heappop(routes)

            # route[_] is:
            # 0, the time taken to access the stockpile, used by the heap
            # 1, the machine ID, which will be its index in the list
            # 2, the position of the stockpile that will enter the machine's route
            # 3, the type of activity that will be performed on the stockpile

            eng: int
            stp: int
            atv: str

            eng, stp, atv = route[1] - 1, route[2], route[3]
            if jobs[stp] != atv and jobs[stp] != 'b':
                if atv == 'b' and jobs[stp] == 's':
                    self._solution.routes[eng].append((stp, 'r'))
                    jobs[stp] = 'b'

                elif atv == 'b' and jobs[stp] == 'r':
                    self._solution.routes[eng].append((stp, 's'))
                    jobs[stp] = 'b'

                else:
                    self._solution.routes[eng].append((stp, atv))
                    jobs[stp] = atv

    def __set_route(
        self: 'SimpleConstructive',
        start_time: List[float],
        engine: Engine
    ) -> Route:
        """This method greedily defines the operating order of each individual 
        machine. It assigns all possible jobs to each machine, which must be 
        further refined by __set_engines().

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

        # list to indicate whether the machine has already visited the stockpile
        visited: List[bool] = [
            False for stp in self._problem.stockpiles 
            if engine.rail in stp.rails
        ]

        # list with machine routes and variable with its starting position
        route: Route = []
        pos: int = engine.pos_ini

        while not all(visited):
            try:
    
                faster: float
                pos: int

                # finds the stockpile with the shortest access time
                faster, pos = min(
                    (time_travel + start_time[engine.id - 1], i)
                    for i, (time_travel, is_visited)
                    in enumerate(zip(self._problem.time_travel[pos], visited))
                    if self._weights[self._output_id][i] > 0 
                        and is_visited is False
                        and engine.rail in self._problem.stockpiles[i].rails
                )

                # indicates which activity will be performed by the machine
                # r to reclaim, s to stack and b to both
                atv: str = 'r'

                # calculates the duration of the job in the stockpile
                duration: float = round(
                    self._weights[self._output_id][pos] / engine.speed_reclaim, 
                    1
                ) if engine.speed_reclaim > 0 else 0

                # if the machine needs to perform the stacking activity
                if self._inputs[pos] > 0:
                    setup_time: float = self._problem.time_travel[pos][pos] \
                        if engine.speed_reclaim > 0 else 0

                    duration += round(
                        self._inputs[pos] / engine.speed_stack, 1
                    ) + setup_time if engine.speed_stack > 0 else 0

                    atv = 's' if engine.speed_stack > 0 else atv
                    atv = 'b' if engine.speed_reclaim > 0 \
                        and engine.speed_stack > 0 else atv

                if duration > 0:
                    # updates the start time list with the operating time
                    start_time[engine.id - 1] += duration + faster

                    # adds data to the referenced engine's route list
                    route.append((faster, engine.id, pos, atv))

                visited[pos] = True

            # if the model is infeasible, the min() function throws an exception
            except ValueError:
                break

        return route

    def __reset_inputs(self: 'SimpleConstructive') -> None:
        """This method is called whenever the input list should be reset 
        (mainly to avoid the need of creating another object).
        """
        
        self._inputs = [
            sum(inp) for inp in list(self._solution.inputs.values())
        ]

    # region simple getters and setters
    @property
    def problem(self: 'SimpleConstructive') -> Problem:
        """Problem: The problem considered."""
        return self._problem

    @problem.setter
    def problem(self: 'SimpleConstructive', value: Problem) -> None:
        self._problem = value

    @property
    def solution(self: 'SimpleConstructive') -> Solution:
        """Solution: The solution reference."""
        return self._solution

    @solution.setter
    def solution(self: 'SimpleConstructive', value: Solution) -> None:
        self._solution = value

    @property
    def output_id(self: 'SimpleConstructive') -> Optional[int]:
        """Optional[int]: The output request identifier."""
        return self._output_id

    @output_id.setter
    def output_id(self: 'SimpleConstructive', value: Optional[int]) -> None:
        self._output_id = value

    @property
    def weights(self: 'SimpleConstructive') -> List[List[float]]:
        """List[List[float]]: List of lists with the weights retrieved from 
        each output request, in which the lines are the requests and the 
        columns, the stockpiles.
        """
        return self._weights

    @weights.setter
    def weights(self: 'SimpleConstructive', value: List[List[float]]) -> None:
        self._weights = value

    @property
    def inputs(self: 'SimpleConstructive') -> List[float]:
        """List[float]: List with the stacked weights, in which the columns are 
        the stockpiles.
        """
        return self._inputs

    @inputs.setter
    def inputs(self: 'SimpleConstructive', value: List[float]) -> None:
        self._inputs = value
