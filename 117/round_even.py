from decimal import Decimal


def round_even(number: float):
    """Takes a number and returns it rounded even"""
    return round(Decimal(number))
