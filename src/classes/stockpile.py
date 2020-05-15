from .quality import Quality
from typing import List


class Stockpile:
    """classe para salvar as informações de cada pilha de minério."""

    def __init__(self,
                 id: int,
                 position: int,
                 capacity: float,
                 engines: List[int],
                 weight_ini: float,
                 quality_ini: List[Quality]):
        self._id = id
        self._position = position
        self._capacity = capacity
        self._engines = engines
        self._weight_ini = weight_ini
        self._quality_ini = quality_ini

    def __repr__(self):
        return f'id: {self._id}\n' + \
               f'position: {self._position}\n' + \
               f'capacity: {self._capacity}\n' + \
               f'engines: {self._engines}\n' + \
               f'weightIni: {self._weight_ini}\n' + \
               f'qualityIni: {self._quality_ini}\n'

    @property
    def id(self) -> int:
        """Stockpile id."""
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def position(self) -> int:
        """Stockpile position."""
        return self._position

    @position.setter
    def position(self, value: int):
        self._position = value

    @property
    def capacity(self) -> float:
        """Stockpile capacity."""
        return self._capacity

    @capacity.setter
    def capacity(self, value: float):
        self._capacity = value

    @property
    def engines(self) -> [int]:
        """Stockpile engines."""
        return self._engines

    @engines.setter
    def engines(self, value: [int]):
        self._engines = value

    @property
    def weight_ini(self) -> float:
        """Stockpile initial weight."""
        return self._weight_ini

    @weight_ini.setter
    def weight_ini(self, value: float):
        self._weight_ini = value

    @property
    def quality_ini(self) -> [Quality]:
        """Stockpile initial quality."""
        return self._quality_ini

    @quality_ini.setter
    def quality_ini(self, value: [Quality]):
        self._quality_ini = value
