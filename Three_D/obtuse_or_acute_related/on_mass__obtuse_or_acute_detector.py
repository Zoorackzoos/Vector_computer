







from Three_D.obtuse_or_acute_related.obtuse_or_acute_detector import obtuse_or_acute_detector

#made of sin
def on_mass__obtuse_or_acute_detector(vector_matrix, tab_amount=""):
    print(f"{tab_amount}on_mass__obtuse_or_acute_detector")
    total_results_list = []

    vector_a_index = 0
    for vector_a in vector_matrix:
        print(f"{tab_amount}\tvector_a_index = {vector_a_index}")
        vector_b_index = vector_a_index + 1
        for vector_b in vector_matrix[vector_a_index+1:]:
            print(f"{tab_amount}\tvector_b_index = {vector_b_index}")
            result = obtuse_or_acute_detector(vector_a, vector_b, tab_amount+"\t")
            total_results_list.append(((vector_a, vector_b), result))
            print(f"{tab_amount}\tback in the 'on_mass__obtuse_or_acute_detector' loop")
            vector_b_index += 1
        vector_a_index += 1

    return total_results_list








