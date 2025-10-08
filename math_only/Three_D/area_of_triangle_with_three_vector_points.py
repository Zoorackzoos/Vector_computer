import math

from math_only.Three_D.ABS_for_vertex_aka_distance_formula import ABS_for_vectors_AKA_distance_formula
from math_only.Three_D.combine_vectors_3d import combine_vectors_3d
from math_only.Three_D.product_name_like_related.dot_product_3d import dot_product_3d
from math_only.Three_D.product_name_like_related.cross_product import cross_product

def area_of_triangle_with_three_vector_points_master(vector_a, vector_b, vector_c, tab_amount):
    """
    P_in_question = (0,1,0)
    Q_in_question = (1,-1,1)
    R_in_question = (-1,1,-1)

    area = 1/2 | PQ x PR |
        PQ = Q_in_question - P_in_question
        PR = R_in_question - P_in_question

    1. make the combination vectors

    PQ
        (1 - 0) + (-1 - 1) + (1 - 0)
        1 + -2 + 1
    PR
        (-1 - 0) + (1 - 1) + (-1 - 0)
        -1 + 0 + -1
            both are vectors so it's ok

    2. cross dot time :-3
        it's read like a arab not like a angloid
    PQ x PR
        =
        |   i   j   k   |
        |   1   -2  1   |
        |   -1   0  -1  |

    i =
        -2  1
        0   -1
            -2 * -1 -> 2
            1 * 0 -> 0
                2 - 0 -> 2
    j =
        1   1
        -1  -1
            1 * -1 -> -1
            1 * -1 -> -1
                -1 - -1 -> 0
    k =
        1   -2
        -1  0
            1 * 0 -> 0
            -2 * -1 -> 2
                0 - 2 -> -2

    (2, 0, -2)

    3. find distance / ABSify it
    sqrt( 2^2 + 0^2 + -2^2 )
    sqrt( 4 + 0 + 4)
    sqrt( 8 )

    4. add the 1/2 cuz formula

    1/2 * sqrt( 8 )

    5. der you go

    :param vector_a:
    :param vector_b:
    :param vector_c:
    :param tab_amount:
    :return:
    """
    print(f"{tab_amount}area_of_triangle_with_three_vector_points_master")
    return_value_for_steps_1_2 = area_of_triangle_with_three_vector_points_steps_1_2(vector_a=vector_a, vector_b=vector_b, vector_c=vector_c, tab_amount=tab_amount+"\t")
    return_value_for_steps_1_2_3_4 = area_of_triangle_with_three_vector_points_steps_3_4(vector_a=return_value_for_steps_1_2, tab_amount=tab_amount+'\t')
    return return_value_for_steps_1_2_3_4

def area_of_triangle_with_three_vector_points_steps_1_2(vector_a, vector_b, vector_c, tab_amount):
    """

    this is:
        1. vector_a + vector_b -> ab
        2. vector_a + vector_c -> ac
        3. AB x AC -> AB_AC_corss_producted
        4. returns AB_AC_corss_producted

    :param vector_a:
    :param vector_b:
    :param vector_c:
    :param tab_amount:
    :return:
    """
    print(f"{tab_amount}area_of_triangle_with_three_vector_points_steps_1_2")
    print(f"{tab_amount}\t1/2 * ( |{vector_a}+{vector_b}| x |{vector_a}+{vector_b}| )")
    print(f"{tab_amount}\t\twe have to get our PQ & PR!")
    PQ = combine_vectors_3d(vector_a=vector_a, vector_b=vector_b, tab_amount=tab_amount + '\t\t\t')
    print(f"{tab_amount}\t\tthat was the end of calculating PQ")
    PR = combine_vectors_3d(vector_a=vector_a, vector_b=vector_c, tab_amount=tab_amount + '\t\t\t')
    print(f"{tab_amount}\t\tthat was the end of calculating PR")
    print()
    print(f"{tab_amount}\t\ttime to to do PQ x PR!")
    result_of_cross_product = cross_product(vertex_a=PQ, vertex_b=PR, tab_amount=tab_amount + '\t\t\t')
    return result_of_cross_product

def area_of_triangle_with_three_vector_points_steps_3_4(vector_a, tab_amount):
    """

    this is:
        1. AB_AC_corss_producted -> AB_AC_corss_product_ABSified
        2. shows you AB_AC_corss_product_ABSified should be sqrt-ed
        3. returns that irrational value.

    it's suggested you input the answer from the terminal lines above
        use
            1/2 * sqrt( # )
        instead of
            1.42948620496872-0548-39
                because nobody knows wtf that is bro

    :param vector_a:
    :param tab_amount:
    :return:
    """

    print(f"{tab_amount}area_of_triangle_with_three_vector_points_steps_3_4")
    print(f"{tab_amount}\t\tresult_of_cross_product = {vector_a}")
    print(f"{tab_amount}\t\ttime to ABSify it / find it's distance.")
    result_of_cross_product_ABSified = ABS_for_vectors_AKA_distance_formula(vertex=vector_a,tab_amount=tab_amount + '\t\t\t')

    print(f"{tab_amount}\t\tresult_of_cross_product_ABSified = sqrt({result_of_cross_product_ABSified})")
    return_value = 1/2 * math.sqrt( result_of_cross_product_ABSified )
    print(f"your answer = {tab_amount}\t1/2 * sqrt({result_of_cross_product_ABSified})")
    return return_value





if __name__ == "__main__":
    review_17_P = [1, 2, 0]
    review_17_Q = [1, 3, 1]
    review_17_R = [-2, 2, 4]

    P_in_question = review_17_P
    Q_in_question = review_17_Q
    R_in_question = review_17_R

    result = area_of_triangle_with_three_vector_points_master(vector_a=P_in_question, vector_b=Q_in_question, vector_c=R_in_question, tab_amount='')
    print(result)














