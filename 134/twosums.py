from itertools import combinations


def two_sums(numbers: list, target: int):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    candidates = [
        (numbers.index(first), numbers.index(second))
        for first, second in combinations(numbers, r=2)
        if first + second == target and first < second
    ]

    result = min(candidates, key=lambda x: numbers[x[0]]) if candidates else None
    return result
