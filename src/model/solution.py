from config import Routes, Weights, Jobs, Deliveries, Result, Qualities, Objective
from model.classes import Request
from .problem import Problem
from typing import Optional, List, Tuple
import numpy as np
import ujson
import os


class Solution:
    """This class represents a Solution of the Machine Scheduling Problem
    and the Ore Mixing Problem.
    """

    def __init__(self: 'Solution', problem: Problem):
        """Instantiates a new Solution.
     
        Args:
            problem (Problem): Problem considered.
        """

        self._problem: Problem = problem

        # Ore Mixing Problem
        self._objective: Optional[float] = None 
        self._weights: Weights = []
        self._inputs: Weights = []

        # Machine Scheduling Problem
        self._cost: float = float('inf')
        self._routes: Routes = [[] for _ in range(len(problem.engines))]
        self._start_time: List[float] = [0] * len(problem.engines)
        self._gap: List[float] = [1] * len(problem.outputs)
        self._stacks: Jobs = []
        self._reclaims: Jobs = []
        self._deliveries: Deliveries = []

        self._has_deliveries: bool = False

    def set_deliveries(self: 'Solution') -> None:
        """This method saves the output data for each order, which consists 
        of the total mass ordered, at the time the order was initiated and 
        its duration, as well as the quality of each ore delivered.
        """
        
        assert self._objective is not None, 'model is infeasible or unbounded.'

        self._has_deliveries = True

        # defines the quality values ​​of each parameter for each order
        self.__quality_mean()

        # iterates over a list of requests to save quality data
        requests: List[List[Request]] = [
            out.quality for out in self._problem.outputs
        ]

        # saves quality data for each parameter of each request
        for req, out in zip(requests, self._problem.outputs):
            quality_list: Qualities = [
                {
                    'parameter': quality.parameter,
                    'value': quality.value,
                    'minimum': quality.minimum, 
                    'maximum': quality.maximum,
                    'goal': quality.goal,
                    'importance': quality.importance
                } for quality in req
            ]

            # calculates the time the request was initiated and completed
            start: float
            end: float

            start, end = self.work_time(out.id)

            # calculates the optimal delivery duration
            optimal_duration: float = out.weight / sum([
                eng.speed_reclaim for eng in self.problem.engines
            ])

            # calculates the gap between the durations
            self._gap[out.id - 1] = round(
                1 - optimal_duration / (end - start),
                2
            )

            # add order information to the delivery list
            self._deliveries.append(
                {
                    'weight': out.weight,
                    'start_time': start,
                    'duration': round(end - start, 2),
                    'quality': quality_list
                }
            )

    def set_objective(self: 'Solution', objective: Objective) -> None:
        """This method sets the objectives for the Machine Scheduling Problem
        from the results of Ore Mixing Problem.

        Args:
            objective (Tuple[Optional[float], Dict[str, List[float]], Dict[str, List[float]]]):
                A tuple whose first element is the objective value of the linear 
                model, the second element is a dictionary of entries whose keys 
                are the stockpiles IDs and values ​​are lists with the stacked 
                weights, the last element is a dictionary of recoveries whose 
                keys are the IDs of each request and the values ​​are lists with 
                the reclaimed weights.
        """

        self._objective = objective[0]
        self._weights = objective[1]
        self._inputs = objective[2]

    def update_cost(self: 'Solution', id: int) -> None:
        """This method calculates and updates the solution cost.
        
        Args:
            id (int): The request identifier.
        """

        self._cost = self.work_time(id)[1]

    def work_time(self: 'Solution', id: int) -> Tuple[float, float]:
        """This method calculates and returns the time the request was 
        initiated and completed.
        
        Args:
            id (int): The request identifier.

        Returns:
            Tuple[float, float]: A tuple which the first value is the start 
                time and the last value is the end time.
        """

        assert self._reclaims, 'calling work_time() for an empty reclaim list.'

        # calculates the time when the request was initiated
        start: float = min(
            [item['start_time'] 
             for item in self._reclaims if item['output'] == id]
        )

        # calculates the time when the request was completed
        end: float = max(
            [item['start_time'] + item['duration']
             for item in self._reclaims if item['output'] == id]
        )

        return start, end

    def write(self: 'Solution', file_path: str) -> None:
        """This method writes the solution in a .json file and, for that, 
        the UltraJSON packege is necessary.
    
        UltraJSON is an ultra fast JSON encoder and decoder written in pure C 
        with bindings for Python 3.5+. To install it just run pip as usual on
        the command prompt:

            $ pip install ujson

        For more information, access https://pypi.org/project/ujson/.

        Args:
            file_path (str): The output file path.
        """

        assert self._has_deliveries, \
            'calling write() before mandatory call to set_deliveries().'

        result: Result = {
            'info': self._problem.info,
            'objective': self._objective,
            'gap': self._gap,
            'stacks': self._stacks,
            'reclaims': self._reclaims,
            'outputs': self._deliveries
        }

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            ujson.dump(result, file, indent=2)

    def reset(self: 'Solution') -> None:
        """This method is called whenever the solution should be reset 
        (mainly to avoid the need of creating another object)."""

        self._stacks = []
        self._reclaims = []
        self._deliveries = []

    def __quality_mean(self: 'Solution') -> None:
        """This method calculates and sets the value of the final quality of 
        each request and, for that, the NumPy package is required.

        NumPy is library that offers comprehensive mathematical functions, 
        random number generators, linear algebra routines, Fourier transforms, 
        and more. To install it just run pip as usual on the command prompt:

            $ pip install numpy

        For more information, access https://numpy.org/.
        """

        assert self._weights, \
            'calling __quality_mean() with a empty list of weights.'

        quality_list: List[List[float]] = [
            [quality.value for quality in stp.quality_ini]  
            for stp in self._problem.stockpiles
        ]

        try:
            # calculates the quality based on the weight taken from each pile
            mean: List[List[float]] = [
                list(np.average(quality_list, axis=0, weights=wl)) 
                for wl in list(self._weights.values())
            ]

            # assigns the calculated quality value to its respective parameter
            for quality, out in zip(mean, self._problem.outputs):
                for value, request in zip(quality, out.quality):
                    request.value = round(value, 2)

        # if the model is infeasible the np.average() function throws an exception
        except ZeroDivisionError:
            raise ZeroDivisionError('the model is infeasible or unbounded.')

    # region simple getters and setters
    @property
    def problem(self: 'Solution') -> Problem:
        """Problem: The problem considered."""
        return self._problem

    @problem.setter
    def problem(self: 'Solution', value: Problem) -> None:
        self._problem = value
    
    @property
    def objective(self: 'Solution') -> Optional[float]:
        """Optional[float]: The solution objective value."""
        return self._objective
    
    @objective.setter
    def objective(self: 'Solution', value: Optional[float]) -> None:
        self._objective = value

    @property
    def weights(self: 'Solution') -> Weights:
        """Dict[str, List[float]]: dictionary of recoveries whose keys are the 
        IDs of each request and the values ​​are lists with the reclaimed weights.
        """
        return self._weights

    @weights.setter
    def weights(self: 'Solution', value: Weights) -> None:
        self._weights = value

    @property
    def inputs(self: 'Solution') -> Weights:
        """Dict[str, List[float]]: dictionary of entries whose keys are the 
        stockpiles IDs and values ​​are lists with the stacked weights.
        """
        return self._inputs

    @inputs.setter
    def inputs(self: 'Solution', value: Weights) -> None:
        self._inputs = value

    @property
    def cost(self: 'Solution') -> float:
        """float: The solution cost."""
        return self._cost

    @cost.setter
    def cost(self: 'Solution', value: float) -> None:
        self._cost = value

    @property
    def routes(self: 'Solution') -> Routes:
        """List[List[Tuple[int, str]]]: Matrix of tuples whose the first
        element is the stockpile position and the last is the engine
        configuration in that stockpile. Each line indicates an engine, 
        based on its IDs.
        """
        return self._routes

    @routes.setter
    def routes(self: 'Solution', value: Routes) -> None:
        self._routes = value

    @property
    def start_time(self: 'Solution') -> List[float]:
        """List[float]: List with the time when each engine can start a new 
        task. The indexes are associated with the IDs of each engine.
        """
        return self._start_time

    @start_time.setter
    def start_time(self: 'Solution', value: List[float]) -> None:
        self._start_time = value

    @property
    def gap(self: 'Solution') -> List[float]:
        """List[float]: List with the gap between the optimal and current
        delivery duration. The indexes are associated with the IDs of each 
        output.
        """
        return self._gap

    @gap.setter
    def gap(self: 'Solution', value: List[float]) -> None:
        self._gap = value

    @property
    def stacks(self: 'Solution') -> Jobs:
        """List[Dict[str, Union[int, float]]]: Dictionary with the stacking 
        data to be recorded in a .json file, in which the keys are the names 
        of the attributes and the values ​​are their information.
        """
        return self._stacks

    @stacks.setter
    def stacks(self: 'Solution', value: Jobs) -> None:
        self._stacks = value

    @property
    def reclaims(self: 'Solution') -> Jobs:
        """List[Dict[str, Union[int, float]]]: Dictionary with the reclaiming 
        data to be recorded in a .json file, in which the keys are the names 
        of the attributes and the values ​​are their information.
        """
        return self._reclaims

    @reclaims.setter
    def reclaims(self: 'Solution', value: Jobs) -> None:
        self._reclaims = value

    @property
    def deliveries(self: 'Solution') -> Deliveries:
        """List[Dict[str, Union[float, List[Dict[str, Union[str, int, float]]]]]]:
        List of dictionaries with the final results, such as delivery time, ore 
        weight, quality parameters and other information for each request.
        """
        return self._deliveries

    @deliveries.setter
    def deliveries(self: 'Solution', value: Deliveries) -> None:
        self._deliveries = value

    @property
    def has_deliveries(self: 'Solution') -> bool:
        """bool: Flag that indicates whether deliveries are defined before 
        writing them to a file.
        """
        return self._has_deliveries

    @has_deliveries.setter
    def has_deliveries(self: 'Solution', value: bool) -> None:
        self._has_deliveries = value
