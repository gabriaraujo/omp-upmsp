class Input:
    def __init__(self, id, source, weight, quality, time):
        self._id = id
        self._source = source
        self._weigth = weight
        self._quality = quality
        self._time = time

    def __repr__(self):
        return f'id: {self._id}\nsource: {self._source}\n' + \
        f'weight: {self._weigth}\nquality: {self._quality}\ntime: {self._time}'

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_source(self, source):
        self._source = source

    def get_source(self):
        return self._source

    def set_weigth(self, weight):
        self._weigth = weight

    def get_weigth(self):
        return self._weigth

    def set_quality(self, quality):
        self._quality = quality

    def get_quality(self):
        return self._quality

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time
