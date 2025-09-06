

"""
only works with parallel & perpenduclar
"""

from print_list import print_list

#made of sin
def convert_vector_pairs_to_names(vector_pairs_list, vector_name_dict, vector_pairs_type):
    nameified_vector_pairs_list = []

    """
    (([3, 1, -1], [1, -3, 0]), 'perpendicular')
    (([3, 1, -1], [1, 0.3333333333333333, 0.3333333333333333]), 'acute')
    (([3, 1, -1], [-3, -1, 1]), 'obtuse')
    (([3, 1, -1], [-1, 3, 0]), 'perpendicular')
    (([1, -3, 0], [1, 0.3333333333333333, 0.3333333333333333]), 'perpendicular')
    (([1, -3, 0], [-3, -1, 1]), 'perpendicular')
    (([1, -3, 0], [-1, 3, 0]), 'obtuse')
    (([1, 0.3333333333333333, 0.3333333333333333], [-3, -1, 1]), 'obtuse')
    (([1, 0.3333333333333333, 0.3333333333333333], [-1, 3, 0]), 'perpendicular')
    (([-3, -1, 1], [-1, 3, 0]), 'perpendicular')
    """
    converted_vector_pairs_list = []
    if vector_pairs_type == "obtuse_or_acute":
        for vector_pair_and_verdict in vector_pairs_list:
            converted_vector_pairs_list.append(vector_pair_and_verdict[0])

    vector_pairs_list__two = []
    if not converted_vector_pairs_list:
        vector_pairs_list__two = vector_pairs_list
    else:
        vector_pairs_list__two = converted_vector_pairs_list

    for vector_pair in vector_pairs_list__two:
        # vector_pair looks like ((1,3,1), (2,-1,0)) for example
        names = []
        for vec in vector_pair:
            if vec in vector_name_dict.values():
                # find the matching key for this vector
                for key, val in vector_name_dict.items():
                    if val == vec:
                        names.append(key)
                        break
        if len(names) == 2:
            nameified_vector_pairs_list.append(list(names))

    if vector_pairs_type == "obtuse_or_acute":
        index = 0
        for vector_pair_and_verdict in vector_pairs_list:
            nameified_vector_pairs_list[index].append( vector_pair_and_verdict[1] )
            index += 1

    return nameified_vector_pairs_list