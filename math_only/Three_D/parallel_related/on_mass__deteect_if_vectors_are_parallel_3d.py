
from print_list import print_list
from math_only.Three_D.parallel_related import detect_if_vectors_are_parallel_3d


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

            temp_result = detect_if_vectors_are_parallel_3d(vector_a=vector_a, vector_b=vector_b, tab_amount=(tab_amount + '\t\t\t'))

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

