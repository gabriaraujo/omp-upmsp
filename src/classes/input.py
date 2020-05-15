from .quality import Quality
from typing import List


class Input:
    """classe para salvar as informações de cada entrada de minério."""

    def __init__(self,
                 id: int,
                 source: int,
                 weight: float,
                 quality: List[Quality],
                 time: float):
        self._id = id
        self._source = source
        self._weight = weight
        self._quality = quality
        self._time = time

    def __repr__(self):
        return f'id: {self._id}\n' + \
               f'source: {self._source}\n' + \
               f'weight: {self._weight}\n' + \
               f'quality: {self._quality}\n' + \
               f'time: {self._time}\n'

    @property
    def id(self) -> int:
        """Input id."""
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def source(self) -> int:
        """Input source."""
        return self._source

    @source.setter
    def source(self, value: int):
        self._source = value

    @property
    def weight(self) -> float:
        """Input weight."""
        return self._weight

    @weight.setter
    def weight(self, value: float):
        self._weight = value

    @property
    def quality(self) -> List[Quality]:
        """Input quality."""
        return self._quality

    @quality.setter
    def quality(self, value: List[Quality]):
        self._quality = value

    @property
    def time(self) -> float:
        """Input time."""
        return self._time

    @time.setter
    def time(self, value: float):
        self._time = value
