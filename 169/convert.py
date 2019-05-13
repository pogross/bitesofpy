def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a float or an int!")

    if fmt.lower() == "cm":
        return round(value * 2.54, 4)
    elif fmt.lower() == "in":
        return round(value * 0.39370079, 4)
    else:
        raise ValueError("Wrong format given!")

