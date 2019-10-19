import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def simple_calculator(calculation: str):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    try:

        first_number, operator, second_number = calculation.split()
        return OPERATORS[operator](int(first_number), int(second_number))

    except (ValueError, ZeroDivisionError, KeyError) as e:
        print(e)
        raise ValueError("This input is not allowed!")
