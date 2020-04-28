from .request import Request


class Output:
    """classe para salvar as informações de cada pedido."""

    def __init__(self,
                 id: int,
                 destination: int,
                 weight: float,
                 quality: [Request],
                 time: float):
        self._id = id
        self._destination = destination
        self._weight = weight
        self._quality = quality
        self._time = time

    def __repr__(self):
        return f'id: {self._id}\n' + \
               f'destination: {self._destination}\n' + \
               f'weight: {self._weight}\n' + \
               f'quality: {self._quality}\n' + \
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
    def quality(self) -> [Request]:
        """Output quality goal."""
        return self._quality

    @quality.setter
    def quality(self, value: [Request]):
        self._quality = value

    @property
    def time(self) -> float:
        """Output time."""
        return self._time

    @time.setter
    def time(self, value: float):
        self._time = value
