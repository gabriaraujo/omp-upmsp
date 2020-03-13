class Output:
    def __init__(self, id, destination, weight, quality_goal,
    quality_upper_limit, quality_lower_limit, time):
        self._id = id
        self._destination = destination
        self._weigth = weight
        self._quality_goal = quality_goal
        self._quality_upper_limit = quality_upper_limit
        self._quality_lower_limit = quality_lower_limit
        self._time = time

    def __repr__(self):
        return f'id: {self._id}\ndestination: {self._destination}\n' + \
        f'weight: {self._weigth}\nqualityGoal: {self._quality_goal}\n' + \
        f'qualityUpperLimit: {self._quality_upper_limit}\n' + \
        f'qualityLowerLimit: {self._quality_lower_limit}\ntime: {self._time}'

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_destination(self, destination):
        self._destination = destination

    def get_destination(self):
        return self._destination

    def set_weigth(self, weight):
        self._weigth = weight

    def get_weigth(self):
        return self._weigth

    def set_quality_goal(self, quality_goal):
        self._quality_goal = quality_goal

    def get_quality_goal(self):
        return self._quality_goal

    def set_quality_upper_limit(self, quality_upper_limit):
        self._quality_upper_limit = quality_upper_limit

    def get_quality_upper_limit(self):
        return self._quality_upper_limit

    def set_quality_lower_limit(self, quality_lower_limit):
        self._quality_lower_limit = quality_lower_limit

    def get_quality_lower_limit(self):
        return self._quality_lower_limit

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time
