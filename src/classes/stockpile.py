from typing import List

class Stockpile:
    def __init__(self, id:int, position, capacity, engines:List[int]):
        self._id = id
        self._position = position
        self._capacity = capacity
        self._engines = engines

    def __repr__(self):
        return f'id: {self._id}\nposition: {self._position}\n' + \
        f'capacity: {self._capacity}\nengines: {self._engines}'
