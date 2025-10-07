import math

from print_list import print_list


def ABS_for_vectors_AKA_distance_formula(vertex,tab_amount):
    """
    This is also called magnitude. finding magnitude
    sqrt( #^2 + #^2 + #^2 )
    fuck the names man.

    :param vertex:
    :param tab_amount:
    :return:
    """

    print(f"{tab_amount}ABS_for_vectors_AKA_distance_formula")
    print(f"{tab_amount}\tsqrt(x^2 + y^2 + z^2)")
    print(f"{tab_amount}\tsqrt({vertex[0]}^2 + {vertex[1]}^2 + {vertex[2]}^2)")
    print(f"{tab_amount}\tsqrt({math.pow(vertex[0],2)} + {math.pow(vertex[1],2)} + {math.pow(vertex[2],2)})")
    print(f"{tab_amount}\tsqrt({math.pow(vertex[0],2)+math.pow(vertex[1],2)+math.pow(vertex[2],2)})")
    output_num = math.pow(vertex[0],2) + math.pow(vertex[1],2) + math.pow(vertex[2],2)
    print(f"{tab_amount}\t{math.sqrt(output_num)}")
    return output_num

if __name__ == "__main__":
    vertex_var = [-4,1,-10]
    vertex_var__1_4_4 = [2,-2,-4]
    vertex_var__1_4_7_force = [0,5,2]
    vertex_var__1_4_8 = [9,0,-9]
    vertex_var__2_5_3 = [12,-4,6]
    vertex_var__2_5_4 = [1,1,1]
    vertex_var__2_5_7 = [-1,-2,-1]

    vertex_var__review_6_v = [3,1,4]
    vertex_var__review_6_w = [2,-2,1]

    vertex_var__review_7_v = [2,3,6]
    vertex_var__review_7_w = [1,-1,1]

    vertex_var__review_8_v = [2, -6, 9]
    vertex_var__review_8_w = [-1,1,-1]

    vertex_var_review_13_v = [2,-2,1]
    vertex_var_review_13_w = [4,0,-3]

    vertex_v_in_question = vertex_var_review_13_v
    vertex_w_in_question = vertex_var_review_13_w

    output_list = []

    output_list.append( ABS_for_vectors_AKA_distance_formula(vertex=vertex_v_in_question,tab_amount="\t") )
    output_list.append( ABS_for_vectors_AKA_distance_formula(vertex=vertex_w_in_question,tab_amount="\t") )

    print_list(list=output_list, tab_amount="")