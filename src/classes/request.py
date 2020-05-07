from .quality import Quality


class Request(Quality):
    """classe para armazenar os dados de qualidade dos pedidos."""

    def __init__(self, 
                 parameter: str,
                 minimum: float,
                 maximum: float,
                 goal: float,
                 importance: int):

        super().__init__(parameter, 0)
        self._minimum = minimum
        self._maximum = maximum
        self._goal = goal
        self._importance = importance

    def __repr__(self):
        return f'parameter: {self._parameter}\n' + \
               f'minimum: {self._minimum}\n' + \
               f'maximum: {self._maximum}\n' + \
               f'goal: {self._goal}\n' + \
               f'importance: {self._importance}\n'

    @property
    def parameter(self) -> str:
        """Request parameter."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: str):
        self._parameter = value

    @property
    def minimum(self) -> float:
        """Request minimum."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: float):
        self._minimum = value

    @property
    def maximum(self) -> float:
        """Request maximum."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: float):
        self._maximum = value

    @property
    def goal(self) -> float:
        """Request goal."""
        return self._goal

    @goal.setter
    def goal(self, value: float):
        self._goal = value

    @property
    def importance(self) -> int:
        """Request importance."""
        return self._importance

    @importance.setter
    def importance(self, value: int):
        self._importance = value
