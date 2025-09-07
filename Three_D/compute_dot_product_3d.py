


def compute_dot_product_3d(vector_a, vector_b, tab_amount):
    """
                           [#,#,#]  [#,#,#]

    :param vector_a:
    :param vector_b:
    :param tab_amount:
    :return:
    """

    print(f"{tab_amount}compute_dot_product_3d")
    print(f"{tab_amount}\t{vector_a}")
    print(f"{tab_amount}\t{vector_b}")
    print(f"{tab_amount}\t\t#x_1 * #x_2 + #y_1 * #y_2 + #z_1 * #z_2")
    print(f"{tab_amount}\t\t{vector_a[0]} * {vector_b[0]} + {vector_a[1]} * {vector_b[1]} + {vector_a[2]} * {vector_b[2]}")
    print(f"{tab_amount}\t\t{vector_a[0] * vector_b[0]} + {vector_a[1] * vector_b[1]} + {vector_a[2] * vector_b[2]}")
    print(f"{tab_amount}\t\t{vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1] + vector_a[2] * vector_b[2]}")

    return (vector_a[0] * vector_b[0]
            +
            vector_a[1] * vector_b[1]
            +
            vector_a[2] * vector_b[2])