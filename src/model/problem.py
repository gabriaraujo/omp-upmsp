from config import Stockpiles, Engines, Inputs, Outputs, Travels
from model.classes import Stockpile, Engine, Input, Output, Quality, Request
from typing import List, Union
import ujson


class Problem:
    """This class represents a Problem that will be used to build 
    the Ore Mixing Problem and the Machine Scheduling Problem from 
    a .json file and, for that, the UltraJSON packege is necessary.
    
    UltraJSON is an ultra fast JSON encoder and decoder written in pure C 
    with bindings for Python 3.5+. To install it just run pip as usual on
    the command prompt:

        $ pip install ujson

    For more information, access https://pypi.org/project/ujson/.
    """

    def __init__(self: 'Problem', instance_path: str):
        """Build a new Problem from a file.
        
        Args:
            instance_path (str): The instance file path.
        """
        
        with open(instance_path, 'r') as file:
            data = ujson.load(file)

        self._info: List[Union[str, int]] = data['info']

        self._stockpiles: Stockpiles = [
            Stockpile(
                data['id'],
                data['position'],
                data['yard'],
                data['rails'],
                data['capacity'],
                data['weightIni'],
                [Quality(*q.values()) for q in data['qualityIni']]
            ) for data in data['stockpiles']
        ]

        self._engines: Engines = [
            Engine(
                data['id'],
                data['speedStack'],
                data['speedReclaim'],
                data['posIni'],
                data['rail'],
                data['yards']
            ) for data in data['engines']
        ]

        self._inputs: Inputs = [
            Input(
                data['id'],
                data['weight'],
                [Quality(*q.values()) for q in data['quality']],
                data['time']
            ) for data in data['inputs']
        ]

        self._outputs: Outputs = [
            Output(
                data['id'],
                data['destination'],
                data['weight'],
                [Request(*q.values()) for q in data['quality']],
                data['time']
            ) for data in data['outputs']
        ]

        self._distances_travel: Travels = data['distancesTravel']
        self._time_travel: Travels = data['timeTravel']

    # region simple getters and setters
    @property
    def info(self: 'Problem') -> List[Union[str, int]]:
        """List[Union[str, int]]: List with the instance name and the omega 
        values for the linear model."""
        return self._info
    
    @info.setter
    def info(self: 'Problem', value: List[Union[str, int]]) -> None:
        self._info = value

    @property
    def stockpiles(self: 'Problem') -> Stockpiles:
        """List[Stockpile]: List with stockpile data."""
        return self._stockpiles

    @stockpiles.setter
    def stockpiles(self: 'Problem', value: Stockpiles) -> None:
        self._stockpiles = value

    @property
    def engines(self: 'Problem') -> Engines:
        """List[Engine]: List with engine data."""
        return self._engines

    @engines.setter
    def engines(self: 'Problem', value: Engines) -> None:
        self._engines = value

    @property
    def inputs(self: 'Problem') -> Inputs:
        """List[Input]: List with ore input data."""
        return self._inputs

    @inputs.setter
    def inputs(self: 'Problem', value: Inputs) -> None:
        self._inputs = value

    @property
    def outputs(self: 'Problem') -> Outputs:
        """List[Output]: list with ore output data."""
        return self._outputs

    @outputs.setter
    def outputs(self: 'Problem', value: Outputs) -> None:
        self._outputs = value

    @property
    def distances_travel(self: 'Problem') -> Travels:
        """List[List[float]]: Matrix with the distances between each stockpile.
        """
        return self._distances_travel

    @distances_travel.setter
    def distances_travel(self: 'Problem', value: Travels) -> None:
        self._distances_travel = value

    @property
    def time_travel(self: 'Problem') -> Travels:
        """List[List[float]]: Matrix with the time needed to travel from one 
        stockpile to another.
        """
        return self._time_travel

    @time_travel.setter
    def time_travel(self: 'Problem', value: Travels) -> None:
        self._time_travel = value
