from print_list import *
from Three_D.compute_dot_product_3d import *
from Three_D.detect_if_vectors_are_parallel_3d import *
from Three_D.detect_if_vectors_are_perpendicular_3d import *
from Three_D.on_mass__detect_if_vectors_are_perpendicular_3d import *
from Two_D import *
from convert_vector_pairs_to_names import *

def on_mass__detect_if_vectors_are_parallel_3d(vector_matrix, tab_amount):
    print(f"{tab_amount}on_mass__detect_if_vectors_are_parallel_3d")
    print(f"{tab_amount}\tvector_matrix:")
    print_list(list=vector_matrix,tab_amount=(tab_amount+'\t\t'))
    print()
    print(f"{tab_amount}\tstarting the \"on_mass__detect_if_vectors_are_parallel_3d\" loop now:")

    parallel_vectors_list = []

    vector_a_index = 0
    vector_b_index = 0

    for vector_a in vector_matrix:
        print(f"{tab_amount}\t\t{vector_a}\t\t\t\t\tvector_a_index = {vector_a_index}")
        for vector_b in vector_matrix[ vector_a_index+1: ]:

            print(f"{tab_amount}\t\t\t{vector_b}\t\t\t\t\t\tvector_b_index = {vector_b_index}")

            temp_result = detect_if_vectors_are_parallel_3d(vector_a=vector_a, vector_b=vector_b, tab_amount=(tab_amount+'\t\t\t'))

            print(f"{tab_amount}\t\t\tback to on_mass__detect_if_vectors_are_parallel_3d 's loop")
            if temp_result:
                temp_list = [vector_b, vector_a] #math and it's backwardsness man. without this "b before a" line the output is incorrect
                if temp_list.reverse() in parallel_vectors_list:
                    print(f"{tab_amount}\t\t\tNot adding pair to parallel_vectors_list because it is already in.")
                else:
                    parallel_vectors_list.append(temp_list)
                    print(f"{tab_amount}\t\t\tadded pair to parallel_vectors_list")
            print()

            vector_b_index += 1
        vector_a_index += 1
    print(f"{tab_amount}\tend of loop")

    print(f"{tab_amount}\tparallel_vectors_list:")
    print_list(list=parallel_vectors_list,tab_amount=(tab_amount+'\t\t'))

    return parallel_vectors_list


"""
1.3 problem 4 
Nice — I can help! Quick plan (tiny and practical): we’ll check pairs one at a time using this method:

Compute the dot product x*y.
    If it equals 0 → vectors are perpendicular.
    If not zero, check parallel by seeing if one vector is a scalar multiple of the other.
    If neither, use the sign of the dot product:
        x * y > 0 --> angle < pi/2 (acute)
        x * y < 0 --> angle > pi/2
"""

def main_function_hehe():
    # my vectors
    a = [3, 1, -1]
    b = [1, -3, 0]
    c = [1, (1 / 3), (1 / 3)]
    d = [-3, -1, 1]
    g = [-1, 3, 0]

    my_vectors__vector_matrix = [a, b, c, d, g]
    my_vectors__vector_matrix__smallest = [a, b]
    my_vectors__vector_matrix__small = [a, b, g]

    my_vectors__name_dict = \
        {"a": a,
         "b": b,
         "c": c,
         "d": d,
         "g": g}

    """
    detect_if_vectors_are_perpendicular_3d(vector_a=a, vector_b=b, tab_amount='')
    detect_if_vectors_are_parallel_3d(vector_a=a, vector_b=c, tab_amount='')
    perpendicular_pairs_list = on_mass__detect_if_vectors_are_perpendicular_3d(vector_matrix=my_vectors__vector_matrix,
                                                                               tab_amount='\t')
    nameified_pairs_list = convert_vector_pairs_to_names(vector_pairs_list=perpendicular_pairs_list,
                                                         vector_name_dict=my_vectors__name_dict)
    
    print_list(list=nameified_pairs_list, tab_amount='')
    """

    parallel_pair_list = on_mass__detect_if_vectors_are_parallel_3d(vector_matrix=my_vectors__vector_matrix,tab_amount="")
    print()
    parallel_pair_list__names = convert_vector_pairs_to_names(vector_pairs_list=parallel_pair_list,vector_name_dict=my_vectors__name_dict)
    print(f"parallel_pair_list__names:")
    print_list(list=parallel_pair_list__names, tab_amount='')

if __name__ == '__main__':
    main_function_hehe()













