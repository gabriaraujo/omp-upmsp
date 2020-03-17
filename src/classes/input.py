class Input:
    """docstring for Input."""

    def __init__(self,
                id: int,
                source: int,
                weight: int,
                quality: [float],
                time: float):
        self._id = id
        self._source = source
        self._weigth = weight
        self._quality = quality
        self._time = time

    def __repr__(self):
        return f'id: {self._id}\n' + \
        f'source: {self._source}\n' + \
        f'weight: {self._weigth}\n' + \
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
        return self._weigth

    @weight.setter
    def weight(self, value: float):
        self._weigth = value

    @property
    def quality(self) -> [float]:
        """Input quality."""
        return self._quality

    @quality.setter
    def quality(self, value: [float]):
        self._quality = value

    @property
    def time(self) -> float:
        """Input time."""
        return self._time

    @time.setter
    def time(self, value: float):
        self._time = value
