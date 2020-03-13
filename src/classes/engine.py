class Engine:
    def __init__(self, id, speed_stack, speed_reclaim, stockpiles):
        self._id = id
        self._speed_stack = speed_stack
        self._speed_reclaim = speed_reclaim
        self._stockpiles = stockpiles

    def __repr__(self):
        return f'id: {self._id}\nspeedStack: {self._speed_stack}\n' + \
        f'speedReclaim: {self._speed_reclaim}\nstockpiles: {self._stockpiles}'

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_speed_stack(self, speed_stack):
        self._speed_stack = speed_stack

    def get_speed_stack(self):
        return self_.speed_stack

    def set_speed_reclaim(self, speed_reclaim):
        self._speed_reclaim = speed_stack

    def get_speed_reclaim(self):
        return self._speed_reclaim

    def set_stockpiles(self, stockpiles):
        self._stockpiles = stockpiles

    def get_stockpiles(self):
        return self._stockpiles
