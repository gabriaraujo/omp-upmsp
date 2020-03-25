class Output:
    """classe para salvar as informações de cada pedido."""

    def __init__(self,
                 id: int,
                 destination: int,
                 weight: float,
                 quality_goal: [float],
                 quality_upper_limit: [float],
                 quality_lower_limit: [float],
                 time: float):
        self._id = id
        self._destination = destination
        self._weight = weight
        self._quality_goal = quality_goal
        self._quality_upper_limit = quality_upper_limit
        self._quality_lower_limit = quality_lower_limit
        self._time = time

    def __repr__(self):
        return f'id: {self._id}\n' + \
               f'destination: {self._destination}\n' + \
               f'weight: {self._weight}\n' + \
               f'qualityGoal: {self._quality_goal}\n' + \
               f'qualityUpperLimit: {self._quality_upper_limit}\n' + \
               f'qualityLowerLimit: {self._quality_lower_limit}\n' + \
               f'time: {self._time}\n'

    @property
    def id(self) -> int:
        """Output id."""
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def destination(self) -> int:
        """Output destination."""
        return self._destination

    @destination.setter
    def destination(self, value: int):
        self._destination = value

    @property
    def weight(self) -> float:
        """Output weight."""
        return self._weight

    @weight.setter
    def weight(self, value: float):
        self._weight = value

    @property
    def quality_goal(self) -> [float]:
        """Output quality goal."""
        return self._quality_goal

    @quality_goal.setter
    def quality_goal(self, value: [float]):
        """Output quality goal."""

    @property
    def quality_upper_limit(self) -> [float]:
        """Output quality upper limit."""
        return self._quality_upper_limit

    @quality_upper_limit.setter
    def quality_upper_limit(self, value: [float]):
        self._quality_upper_limit = value

    @property
    def quality_lower_limit(self) -> [float]:
        """Output quality lower limit."""
        return self._quality_lower_limit

    @quality_lower_limit.setter
    def quality_lower_limit(self, value: [float]):
        self._quality_lower_limit = value

    @property
    def time(self) -> float:
        """Output time."""
        return self._time

    @time.setter
    def time(self, value: float):
        self._time = value
