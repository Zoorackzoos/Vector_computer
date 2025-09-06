


def detect_if_vectors_are_parallel_3d(vector_a, vector_b, tab_amount):
    """
    might be something i missed. the previous function dealt with matrix's full of these

    x2  =   y2  =   z2
    /       /       /
    x1      y1      z1

    :param vector_a:
    :param vector_b:
    :param tab_amount:
    :return:
    """
    print(f"{tab_amount}detect_if_vectors_are_parallel")
    print(f"{tab_amount}\tvector_a = {vector_a}")
    print(f"{tab_amount}\tvector_b = {vector_b}")
    print(f"{tab_amount}\tx_2\ty_2\tz_2\t\t\t{vector_b[0]}\t{vector_b[1]}\t{vector_b[2]}")
    print(f"{tab_amount}\t///\t///\t///\t\t\t///\t///\t///")
    print(f"{tab_amount}\tx_1\ty_1\tz_1\t\t\t{vector_a[0]}\t{vector_a[1]}\t{vector_a[2]}")
    print()

    parallelness_bool = False
    parallelness_bool__x = False
    parallelness_bool__y = False
    parallelness_bool__z = False

    divide_by_zero_bool__x__bad = \
        (
            (vector_a[0] == 0 and vector_b[0] != 0)
            or
            (vector_a[0] != 0 and vector_b[0] == 0)
        )
    divide_by_zero_bool__y__bad = \
        (
            (vector_a[1] == 0 and vector_b[1] != 0)
            or
            (vector_a[1] != 0 and vector_b[1] == 0)
        )
    divide_by_zero_bool__z__bad = \
        (
            (vector_a[2] == 0 and vector_b[2] != 0)
            or
            (vector_a[2] != 0 and vector_b[2] == 0)
        )

    divide_by_zero_bool__x__good = \
        (
            (vector_a[0] == 0 and vector_b[0] == 0)
        )
    divide_by_zero_bool__y__good = \
        (
            (vector_a[1] == 0 and vector_b[1] == 0)
        )
    divide_by_zero_bool__z__good = \
        (
            (vector_a[2] == 0 and vector_b[2] == 0)
        )

    if divide_by_zero_bool__x__bad:
        parallelness_bool__x = False
    elif divide_by_zero_bool__x__good:
        parallelness_bool__x = True
    else:
        parallelness_bool__x = abs( vector_a[0] / vector_b[0] )

    if divide_by_zero_bool__y__bad:
        parallelness_bool__y = False
    elif divide_by_zero_bool__y__good:
        parallelness_bool__y = True
    else:
        parallelness_bool__y = abs( vector_a[1] / vector_b[1] )

    if divide_by_zero_bool__z__bad:
        parallelness_bool__z = False
    elif divide_by_zero_bool__z__good:
        parallelness_bool__z = True
    else:
        parallelness_bool__z = abs( vector_a[2] / vector_b[2] )

    if parallelness_bool__x and parallelness_bool__y and parallelness_bool__z:
        parallelness_bool = True

    print(f"{tab_amount}\t{parallelness_bool}")

    return parallelness_bool