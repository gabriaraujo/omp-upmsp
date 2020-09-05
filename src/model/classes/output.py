from .request import Request
from typing import List


class Output:
    """This class represents an ore Output. The attributes indicate the weight 
    of ore requested in the output, the quality parameters of these ores and 
    when the output request can be started."""

    def __init__(
        self: 'Input',
        id: int,
        destination: int,
        weight: float,
        quality: List[Request],
        time: float
    ):
        """Instantiates a new Output.

        Args:
            id (int): The output identifier.
            destination (int): The destination identifier of the output.
            weight (float): The weight of ore requested in the output.
            quality (List[Request]): List with the requested quality parameters.
            time (float): Time when the output request can be started.
        """
        self._id: int = id
        self._destination: int = destination
        self._weight: float = weight
        self._quality: List[Request] = quality
        self._time: float = time

    def __repr__(self: 'Input') -> str:
        """This method returns the string representation of an Output.
        
        Returns:
            str: The string representation of this class.
        """

        return f'id: {self._id}\n' + \
               f'destination: {self._destination}\n' + \
               f'weight: {self._weight}\n' + \
               f'quality: {self._quality}\n' + \
               f'time: {self._time}\n'

    # region simple getters and setters
    @property
    def id(self: 'Input') -> int:
        """int: The output identifier."""
        return self._id

    @id.setter
    def id(self: 'Input', value: int) -> None:
        self._id = value

    @property
    def destination(self: 'Input') -> int:
        """int: The destination identifier of the output."""
        return self._destination

    @destination.setter
    def destination(self: 'Input', value: int) -> None:
        self._destination = value

    @property
    def weight(self: 'Input') -> float:
        """float: The weight of ore requested in the output."""
        return self._weight

    @weight.setter
    def weight(self: 'Input', value: float) -> None:
        self._weight = value

    @property
    def quality(self: 'Input') -> List[Request]:
        """List[Request]: List with the requested quality parameters."""
        return self._quality

    @quality.setter
    def quality(self: 'Input', value: List[Request]) -> None:
        self._quality = value

    @property
    def time(self: 'Input') -> float:
        """float: Time when the output request can be started."""
        return self._time

    @time.setter
    def time(self: 'Input', value: float) -> None:
        self._time = value
