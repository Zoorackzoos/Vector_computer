import math
from math_only.number_simplifiers.sqrt_checker_function_ijk_components import sqrt_checker_function_ijk_components
from math_only.Three_D.combine_vectors_3d import combine_vectors_3d

def cross_product(vertex_a, vertex_b, tab_amount):
    """
    v = -3i - k - 3k
    w = 2i - j + 3k

    le matrix_      X & Y & Z
        A   B
        C   D
    read like an angloid
        left to right
            IT'S LEFT TO RIGHT
            NOT RIGHT TO LEFT
            HOLY FUCK

    

    Rince & repeat until you get x, y & z

    :param vertex_a:
    :param vertex_b:
    :param tab_amount:
    :return:
    """
    print(f"{tab_amount}algebraic_dot_product")
    print(f"{tab_amount}\tv * w = ")
    print(f"{tab_amount}\t\t|\ti\tj\tk\t|")
    print(f"{tab_amount}\t\t|\t{vertex_a[0]}\t{vertex_a[1]}\t{vertex_a[2]}\t|")
    print(f"{tab_amount}\t\t|\t{vertex_b[0]}\t{vertex_b[1]}\t{vertex_b[2]}\t|")
    print()

    print(f"{tab_amount}\t\ti_component = ")
    print(f"{tab_amount}\t\t\t{vertex_a[1]}\t{vertex_a[2]}")
    print(f"{tab_amount}\t\t\t{vertex_b[1]}\t{vertex_b[2]}")
    print(f"{tab_amount}\t\t\t\t{vertex_a[1]} * {vertex_b[2]} - {vertex_a[2]} * {vertex_b[1]}")
    print(f"{tab_amount}\t\t\t\t{vertex_a[1] * vertex_b[2]} - {vertex_a[2] * vertex_b[1]}")
    i_component =               (vertex_a[1] * vertex_b[2]  - vertex_a[2] * vertex_b[1])
    print(f"{tab_amount}\t\t\t\t{i_component}")

    print(f"{tab_amount}\t\tj_component = ")
    print(f"{tab_amount}\t\t\t{vertex_a[0]}\t{vertex_a[2]}")
    print(f"{tab_amount}\t\t\t{vertex_b[0]}\t{vertex_b[2]}")
    print(f"{tab_amount}\t\t\t\t-1 * ({vertex_a[0]} * {vertex_b[2]} - {vertex_a[2]} * {vertex_b[0]})")
    print(f"{tab_amount}\t\t\t\t-1 * ({vertex_a[0] * vertex_b[2]} - {vertex_a[2] * vertex_b[0]})")
    j_component =             -1 * ( (vertex_a[0] * vertex_b[2]) - (vertex_a[2] * vertex_b[0]) )
    print(f"{tab_amount}\t\t\t\t{j_component}")

    print(f"{tab_amount}\t\tk_component = ")
    print(f"{tab_amount}\t\t\t{vertex_a[0]}\t{vertex_a[1]}")
    print(f"{tab_amount}\t\t\t{vertex_b[0]}\t{vertex_b[1]}")
    print(f"{tab_amount}\t\t\t\t{vertex_a[0]} * {vertex_b[1]} - {vertex_a[1]} * {vertex_b[0]}")
    print(f"{tab_amount}\t\t\t\t{vertex_a[0] * vertex_b[1]} - {vertex_a[1] * vertex_b[0]}")
    k_component =               (vertex_a[0] * vertex_b[1] - vertex_a[1] * vertex_b[0])
    print(f"{tab_amount}\t\t\t\t{k_component}")

    i_component, j_component, k_component = (
        sqrt_checker_function_ijk_components(i_component, j_component, k_component, tab_amount=tab_amount + '\t'))

    output_list = [i_component, j_component, k_component]
    return output_list





if __name__ == '__main__':

    v_1 = [1,2,3]
    w_1 = [4,5,6]

    v_2 = [0,1,0]
    w_2 = [ (-9/math.sqrt(2)) , (9/math.sqrt(2)) , 0]

    v_1_4_8 = [1,3,1]
    w_1_4_8 = [1,12,1]

    v_1_5_7__pq = [1,-2,1]
    w_1_5_7__pr = [-1,0,-1]

    v_1_5_8__1 = [3,5,-6]
    w_1_5_8__2 = [2,1,4]

    v_1_5_9__1 = [-1,3,-3]
    w_1_5_9__2 = [3,-2,1]

    calc_3_review__15_pq = [2,0,2]
    calc_3_review__15_pr = [1,-1,1]

    v_in_question = calc_3_review__15_pq
    w_in_question = calc_3_review__15_pr

    result = cross_product(v_in_question, w_in_question, tab_amount="")
    print(result)













