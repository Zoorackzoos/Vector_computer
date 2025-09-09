

def compute_dot_product_2d(vector_a, vector_b, tab_amount):
    """
                               [#,#]   [#,#]

    :param vector_a:
    :param vector_b:
    :param tab_amount:
    :return:
    """

    print(f"{tab_amount}compute_dot_product_2d")
    print(f"{tab_amount}\t{vector_a}")
    print(f"{tab_amount}\t{vector_b}")
    print(f"{tab_amount}\t\t#x_1 * #x_2 + #y_1 * #y_2")
    print(f"{tab_amount}\t\t{vector_b[0]} * {vector_a[0]} + {vector_b[1]} * {vector_a[1]}")
    print(f"{tab_amount}\t\t{vector_b[0] * vector_a[0]} + {vector_b[1] * vector_a[1]}")

    return (vector_b[0] * vector_a[0]
            +
            vector_b[1] * vector_a[1])