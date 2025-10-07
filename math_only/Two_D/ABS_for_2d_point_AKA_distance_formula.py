import math

from print_list import print_list


def ABS_for_2d_point_AKA_distance_formula(_2d_point, tab_amount):
    print(f"{tab_amount}ABS_for_2d_point_AKA_distance_formula")
    print(f"{tab_amount}\tsqrt(x^2 + y^2)")
    print(f"{tab_amount}\tsqrt({_2d_point[0]}^2 + {_2d_point[1]}^2)")
    print(f"{tab_amount}\tsqrt({math.pow(_2d_point[0], 2)} + {math.pow(_2d_point[1], 2)})")
    print(f"{tab_amount}\tsqrt({math.pow(_2d_point[0], 2) + math.pow(_2d_point[1], 2)})")
    output_num = math.pow(_2d_point[0], 2) + math.pow(_2d_point[1], 2)
    print(f"{tab_amount}\t{math.sqrt(output_num)}")
    return output_num

if __name__ == "__main__":
    calc_3_review__5_u = [2,3]
    calc_3_review__5_v = [5,12]

    output_list = []

    output_list.append( ABS_for_2d_point_AKA_distance_formula( _2d_point=calc_3_review__5_u , tab_amount="") )
    output_list.append( ABS_for_2d_point_AKA_distance_formula( _2d_point=calc_3_review__5_v , tab_amount="") )

    print_list(list=output_list, tab_amount="")