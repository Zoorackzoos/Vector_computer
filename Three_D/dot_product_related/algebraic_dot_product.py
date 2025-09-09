import math
from sympy import symbols, sqrt, simplify, nsimplify

from convert_to_divided_by_sqrt import convert_to_divided_by_sqrt


def algebraic_dot_product(vertex_a, vertex_b, tab_amount):
    """
    v = -3i - k - 3k
    w = 2i - j + 3k

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
    i_component = (vertex_a[1] * vertex_b[2]) - (vertex_a[2] * vertex_b[1])
    print(f"{tab_amount}\t\t\t\t{i_component}")

    print(f"{tab_amount}\t\tj_component = ")
    print(f"{tab_amount}\t\t\t{vertex_a[0]}\t{vertex_a[2]}")
    print(f"{tab_amount}\t\t\t{vertex_b[0]}\t{vertex_b[2]}")
    print(f"{tab_amount}\t\t\t\t-1 * {vertex_a[0]} * {vertex_b[2]} - {vertex_a[2]} * {vertex_b[0]}")
    print(f"{tab_amount}\t\t\t\t-1 * {vertex_a[0] * vertex_b[2]} - {vertex_a[2] * vertex_b[0]}")
    j_component = -1 * ( (vertex_a[0] * vertex_b[2]) - (vertex_a[2] * vertex_b[0]) )
    print(f"{tab_amount}\t\t\t\t{j_component}")

    print(f"{tab_amount}\t\tk_component = ")
    print(f"{tab_amount}\t\t\t{vertex_a[0]}\t{vertex_a[1]}")
    print(f"{tab_amount}\t\t\t{vertex_b[0]}\t{vertex_b[1]}")
    print(f"{tab_amount}\t\t\t\t{vertex_a[0]} * {vertex_b[1]} - {vertex_a[1]} * {vertex_b[0]}")
    print(f"{tab_amount}\t\t\t\t{vertex_a[0] * vertex_b[1]} - {vertex_a[1] * vertex_b[0]}")
    k_component = (vertex_a[0] * vertex_b[1]) - (vertex_a[1] * vertex_b[0])
    print(f"{tab_amount}\t\t\t\t{k_component}")

    i_component, j_component, k_component = sqrt_checker_funciton(i_component, j_component, k_component, tab_amount=tab_amount+'\t')

    output_list = [i_component, j_component, k_component]
    return output_list


def sqrt_checker_funciton(i_component, j_component, k_component, tab_amount):
    print(f"{tab_amount}sqrt_checker_funciton")
    i_component_unsimplified = convert_to_divided_by_sqrt(i_component,tab_amount=tab_amount+'\t')
    j_component_unsimplified = convert_to_divided_by_sqrt(j_component,tab_amount=tab_amount+'\t')
    k_component_unsimplified = convert_to_divided_by_sqrt(k_component,tab_amount=tab_amount+'\t')
    if i_component_unsimplified != None:
        i_component = i_component_unsimplified
    if j_component_unsimplified != None:
        j_component = j_component_unsimplified
    if k_component_unsimplified != None:
        k_component = k_component_unsimplified
    return i_component, j_component, k_component


if __name__ == '__main__':

    v_1 = [1,2,3]
    w_1 = [4,5,6]

    v_2 = [0,1,0]
    w_2 = [ (-9/math.sqrt(2)) , (9/math.sqrt(2)) , 0]

    v_in_question = v_2
    w_in_question = w_2

    result = algebraic_dot_product(v_in_question, w_in_question, tab_amount="")
    print(result)














