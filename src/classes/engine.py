from typing import List

class Engine:
    """classe para salvar as informações de cada equipamento."""

    def __init__(self,
                 id: int,
                 speed_stack: float,
                 speed_reclaim: float,
                 pos_ini: int,
                 rail: int,
                 yards: List[int]):
        self._id = id
        self._speed_stack = speed_stack
        self._speed_reclaim = speed_reclaim
        self._pos_ini = pos_ini
        self._rail = rail
        self._yards = yards

    def __repr__(self):
        return f'id: {self._id}\n' + \
               f'speedStack: {self._speed_stack}\n' + \
               f'speedReclaim: {self._speed_reclaim}\n' + \
               f'posIni: {self._pos_ini}\n' + \
               f'rail: {self._rail}\n' + \
               f'yards: {self._yards}\n'

    @property
    def id(self) -> int:
        """Engine id."""
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def speed_stack(self) -> float:
        """Engine speed stack."""
        return self._speed_stack

    @speed_stack.setter
    def speed_stack(self, value: float):
        self._speed_stack = value

    @property
    def speed_reclaim(self) -> float:
        """Engine speed reclaim."""
        return self._speed_reclaim

    @speed_reclaim.setter
    def speed_reclaim(self, value: float):
        self._speed_reclaim = value

    @property
    def pos_ini(self) -> int:
        """Engine initial position."""
        return self._pos_ini

    @pos_ini.setter
    def pos_ini(self, value: int):
        self._pos_ini = value

    @property
    def rail(self) -> int:
        """"Engine rail."""
        return self._rail

    @rail.setter
    def rail(self, value: int):
        self._rail = value

    @property
    def yards(self) -> List[int]:
        """Engine yards."""
        return self._yards

    @yards.setter
    def yards(self, value: List[int]):
        self._yards = value
