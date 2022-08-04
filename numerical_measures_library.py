class NumericalMeasuresLibrary:
    @staticmethod
    def generate_frequency_map(data_points: list):
        results = {}
        for point in data_points:
            if point in results.keys():
                results[point] += 1
            else:
                results[point] = 1
        return results

    @staticmethod
    def calculate_mean(data_points: list):
        return sum(data_points) / len(data_points)

    @staticmethod
    def calculate_qs(data_points: list):
        median_and_sliced_lists = NumericalMeasuresLibrary.calculate_median(data_points=data_points)
        q1 = NumericalMeasuresLibrary.calculate_median(data_points=median_and_sliced_lists[1])[0]
        q2 = median_and_sliced_lists[0]
        q3 = NumericalMeasuresLibrary.calculate_median(data_points=median_and_sliced_lists[2])[0]
        return q1, q2, q3

    @staticmethod
    def calculate_median(data_points: list):
        n = len(data_points)
        if n > 1:
            middle_idx = n // 2
            if is_even(n):
                first_half_list = data_points[:middle_idx]
                second_half_list = data_points[middle_idx:]
                first_value = data_points[middle_idx - 1]
                second_value = data_points[middle_idx]
                median = (first_value + second_value) / 2
                return median, first_half_list, second_half_list
            else:
                first_half_list = data_points[:middle_idx]
                second_half_list = data_points[middle_idx + 1:]
                median = data_points[middle_idx]
                return median, first_half_list, second_half_list

    @staticmethod
    def calculate_mode(frequency_map: dict):
        max_repetition = max(frequency_map.values())
        mode = [key for key, value in frequency_map.items() if value == max_repetition]
        if len(mode) < len(frequency_map):
            return mode
        return []

    @staticmethod
    def calculate_iqr(q1: float, q3: float):
        return q3 - q1

    @staticmethod
    def calculate_range(maximum: float, minimum: float):
        return maximum - minimum

    @staticmethod
    def calculate_max(data_points: list):
        return max(data_points)

    @staticmethod
    def calculate_min(data_points: list):
        return min(data_points)


def is_even(entry):
    return entry % 2 == 0


def is_odd(entry):
    return entry % 2 == 1
