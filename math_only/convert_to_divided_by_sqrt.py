from pandas.core.dtypes.inference import is_integer
from math_only.get_decimal_length import get_decimal_length

#made of sin
def convert_to_divided_by_sqrt(number,tab_amount, tolerance=1e-6, max_check=20):
    print(f"{tab_amount}convert_to_divided_by_sqrt")
    if is_integer(number):
        print(f"{tab_amount}\tit's a integer so there's no sqrt risk")
        return None
    if get_decimal_length(number) <= 3:
        print(f"{tab_amount}\tthe decimal length of {number} is too small")
    else:
        print(f"{tab_amount}\tit's not a integer. maybe a sqrt.")
        for a in range(1, max_check):
            for b in range(1, max_check):
                candidate = a / (b ** 0.5)
                if abs(candidate - number) < tolerance:
                    return f"{a}/sqrt({b})"
        return None