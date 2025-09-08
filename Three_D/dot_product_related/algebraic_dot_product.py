import math
from sympy import symbols, sqrt, simplify, nsimplify


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


    i_component = nsimplify(i_component,rational=True)
    j_component = nsimplify(j_component,rational=True)
    k_component = nsimplify(k_component,rational=True)

    i_component = simplify(i_component)
    j_component = simplify(j_component)
    k_component = simplify(k_component)


    output_list = [i_component, j_component, k_component]
    return output_list

if __name__ == '__main__':

    v_in_question = [0,1,0]
    w_in_question = [ (-9/math.sqrt(2)) , (9/math.sqrt(2)) , 0]

    print( algebraic_dot_product(v_in_question, w_in_question, tab_amount="") )
    print()
    print()
    print()

def convert_poopoo_number_into_peepee_number(number,tab_amount):
    from sympy import symbols, sqrt, simplify, Rational, nsimplify

    # Input: numerical value
    num = float(input("Enter the number: "))

    # Try to detect a / sqrt(b) pattern
    def detect_over_sqrt(x, tolerance=1e-6, max_check=20):
        for a in range(1, max_check):
            for b in range(1, max_check):
                candidate = a / (b ** 0.5)
                if abs(candidate - x) < tolerance:
                    return f"{a}/sqrt({b})"
        return None

    result = detect_over_sqrt(num)

    if result:
        print("Detected symbolic form:", result)
    else:
        print("Could not detect simple a/sqrt(b) form")














