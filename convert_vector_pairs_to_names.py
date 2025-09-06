


#made of sin
def convert_vector_pairs_to_names(vector_pairs_list, vector_name_dict):
    nameified_vector_pairs_list = []

    for vector_pair in vector_pairs_list:
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
            nameified_vector_pairs_list.append(tuple(names))

    return nameified_vector_pairs_list