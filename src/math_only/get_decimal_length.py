def get_decimal_length(number):
    """
    Calculates the number of digits after the decimal point in a float.

    Args:
        number (float): The floating-point number.

    Returns:
        int: The number of digits after the decimal point.
    """
    s = str(number)
    if '.' in s:
        return len(s) - s.find('.') - 1
    else:
        return 0