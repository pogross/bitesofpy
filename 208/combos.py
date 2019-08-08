from itertools import combinations


def find_number_pairs(numbers: list, N: int = 10) -> list:
    pairs = combinations(numbers, 2)
    return [pair for pair in pairs if sum(pair) == N]
