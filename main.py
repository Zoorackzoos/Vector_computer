from math_only.Three_D.obtuse_or_acute_related.on_mass__obtuse_or_acute_detector import on_mass__obtuse_or_acute_detector
from math_only.convert_vector_pairs_to_names import *

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

    """
    parallel_pair_list = on_mass__detect_if_vectors_are_parallel_3d(vector_matrix=my_vectors__vector_matrix,tab_amount="")
    print()
    parallel_pair_list__names = convert_vector_pairs_to_names(vector_pairs_list=parallel_pair_list,vector_name_dict=my_vectors__name_dict)
    print(f"parallel_pair_list__names:")
    print_list(list=parallel_pair_list__names, tab_amount='')
    """

    obtuse_or_actue_list = on_mass__obtuse_or_acute_detector(vector_matrix=my_vectors__vector_matrix,tab_amount="")
    obtuse_or_acute_list_names = convert_vector_pairs_to_names(vector_pairs_list=obtuse_or_actue_list,vector_name_dict=my_vectors__name_dict,vector_pairs_type="obtuse_or_acute")
    print()
    print("obtuse_or_actue_list__names:")
    print_list(list=obtuse_or_acute_list_names, tab_amount='')

if __name__ == '__main__':
    main_function_hehe()













