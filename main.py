from numerical_measures_calculator import NumericalMeasuresCalculator

if __name__ == '__main__':
    points1 = [1, 3, 4, 12, 17, 22, 99, 31, 34, 41, 41, 71, 72, 99]
    points2 = [2, 8, 13, 14, 16, 18, 18, 23, 42, 46]
    points3 = [2, 15, 16, 16, 18, 22, 24, 38, 45]
    points4 = [1, 3, 7, 19, 20, 29, 34, 37]
    points5 = [1, 7, 17, 24, 39, 40, 42, 46, 49]
    nmc = NumericalMeasuresCalculator(entries=points1)
    print(nmc)
    nmc.points = []
    print(nmc)
    nmc.points = points5
    print(nmc)
