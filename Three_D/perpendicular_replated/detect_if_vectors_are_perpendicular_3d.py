
from Three_D.compute_dot_product_3d import compute_dot_product_3d


def detect_if_vectors_are_perpendicular_3d(vector_a, vector_b, tab_amount):
    """

    1st return = the numerical result of the dot product
    2nd return = the bool that says if it's perpendicular or not.
                 you can tell based off the number but you get the bool anyway

    :param vector_a:
    :param vector_b:
    :param tab_amount:
    :return:
    """
    print(f"{tab_amount}detect_if_vectors_are_perpendicular_3d")
    result_of_dot_product = compute_dot_product_3d(vector_a=vector_a, vector_b=vector_b, tab_amount=(tab_amount+'\t'))
    print(f"{tab_amount}\tresult_of_dot_product = {result_of_dot_product}")

    if_zero_bool = result_of_dot_product == 0

    print(f"{tab_amount}\t({result_of_dot_product} == 0) ?      is perpendicular?")
    print(f"{tab_amount}\t\t{if_zero_bool}")
    #           number                bool
    return result_of_dot_product, if_zero_bool
