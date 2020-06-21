from .quality import Quality
from typing import List


class Stockpile:
    """classe para salvar as informações de cada pilha de minério."""

    def __init__(self,
                 id: int,
                 position: int,
                 yard: int,
                 rails: List[int],
                 capacity: float,
                 weight_ini: float,
                 quality_ini: List[Quality]):
        self._id = id
        self._position = position
        self._yard = yard
        self._rails = rails
        self._capacity = capacity
        self._weight_ini = weight_ini
        self._quality_ini = quality_ini

    def __repr__(self):
        return f'id: {self._id}\n' + \
               f'position: {self._position}\n' + \
               f'yard: {self._yard}\n' + \
               f'rails: {self._rails}\n' + \
               f'capacity: {self._capacity}\n' + \
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
    def yard(self) -> int:
        """Stockpile yard."""
        return self._yard

    @yard.setter
    def yard(self, value):
        self._yard = value

    @property
    def rails(self) -> List[int]:
        """Stockpile rails."""
        return self._rails

    @rails.setter
    def rails(self, value):
        self._rails = value

    @property
    def capacity(self) -> float:
        """Stockpile capacity."""
        return self._capacity

    @capacity.setter
    def capacity(self, value: float):
        self._capacity = value

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
