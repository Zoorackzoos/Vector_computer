from math_only.Three_D.ABS_for_vertex_aka_distance_formula import ABS_for_vectors_AKA_distance_formula
from math_only.Three_D.product_name_like_related.cross_product import cross_product
from print_list import print_list

def get_perpendicular_vector_from_two_vectors(vector_a,vector_b,tab_amount):
    print(f"{tab_amount}get_perpendicular_vector_from_two_vectors")

    result_of_cross_product = \
        (cross_product
         (vertex_a=vector_a, vertex_b=vector_b, tab_amount=tab_amount + '\t'))

    print(f"{tab_amount}\t{result_of_cross_product}")

    result_of_cross_product_ABSified = \
        (ABS_for_vectors_AKA_distance_formula
            (vertex=result_of_cross_product, tab_amount=tab_amount + '\t')
        )

    print(f"{tab_amount}\t{result_of_cross_product_ABSified}")

    """
    return_list = \
            [
            result_of_cross_product[0]/math.sqrt(result_of_cross_product_ABSified)
            ,
            result_of_cross_product[1]/math.sqrt(result_of_cross_product_ABSified)
            ,
            result_of_cross_product[2]/math.sqrt(result_of_cross_product_ABSified)
            ]
    print(f"{tab_amount}\t{return_list}")
    """
    return_list_string = \
            [
                str(result_of_cross_product[0]) + " / sqrt(" + str(result_of_cross_product_ABSified + ")")
            ,
                str(result_of_cross_product[1]) + " / sqrt(" + str(result_of_cross_product_ABSified + ")")
            ,
                str(result_of_cross_product[2]) + " / sqrt(" + str(result_of_cross_product_ABSified + ")")
            ]

    print_list(list=return_list_string,tab_amount=f"{tab_amount}\t")

    return return_list_string

if __name__ == "__main__":
    v_1_4_8 = [1,3,1]
    w_1_4_8 = [1,12,1]

    get_perpendicular_vector_from_two_vectors(vector_a=v_1_4_8,vector_b=w_1_4_8,tab_amount='')
