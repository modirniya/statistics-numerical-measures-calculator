from numerical_measures_library import NumericalMeasuresLibrary as Lib


class NumericalMeasuresCalculator:

    def __init__(self, entries: list):
        self.points = entries
        self.__allocate_properties()

    def __allocate_properties(self):
        self.__data_points.sort()
        self.__frequency_map = \
            Lib.generate_frequency_map(self.points)
        self.__mean: float = Lib.calculate_mean(data_points=self.points)
        self.__q1, self.__median, self.__q3 = Lib.calculate_qs(data_points=self.points)
        self.__mode: list = Lib.calculate_mode(frequency_map=self.frequency_map)
        self.__iqr: float = Lib.calculate_iqr(q1=self.q1, q3=self.q3)
        self.__max: float = Lib.calculate_max(data_points=self.points)
        self.__min: float = Lib.calculate_min(data_points=self.points)
        self.__range: float = Lib.calculate_range(maximum=self.maximum, minimum=self.minimum)

    def get_points(self):
        return self.__data_points

    def set_points(self, entries):
        if len(entries) < 1:
            print('invalid dataset provided.')
            return
        self.__data_points = entries
        self.__allocate_properties()

    points = property(get_points, set_points)

    def get_q1(self):
        return self.__q1

    q1 = property(get_q1)

    # Q2 linked with median

    def get_q3(self):
        return self.__q3

    q3 = property(get_q3)

    def get_iqr(self):
        return self.__iqr

    iqr = property(get_iqr)

    def get_min(self):
        return self.__min

    minimum = property(get_min)

    def get_range(self):
        return self.__range

    range = property(get_range)

    def get_n(self):
        return len(self.points)

    def get_max(self):
        return self.__max

    maximum = property(get_max)

    def get_mean(self):
        return self.__mean

    mean = property(get_mean)

    def get_median(self):
        return self.__median

    q2 = property(get_median)
    median = property(get_median)

    def get_mode(self):
        return self.__mode

    mode = property(get_mode)

    def get_n(self):
        return len(self.__data_points)

    n = property(get_n)

    def get_frequency_map(self):
        return self.__frequency_map

    frequency_map = property(get_frequency_map)

    def __str__(self):
        return f'''
    Sorted list          => {self.points}
    Frequency map        => {self.frequency_map}
    Five number summary  => [{self.minimum}, {self.q1}, {self.q2}, {self.q3}, {self.maximum}]
    Length (n)           => {self.n}
    Mean(Average)        => {self.mean}
    Median               => {self.median}
    Mode                 => {self.mode}
    IQR                  => {self.iqr}
    Range                => {self.range}
    Minimum              => {self.minimum}
    Maximum              => {self.maximum}
        '''


