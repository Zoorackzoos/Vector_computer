import math
from print_list import print_list


def distance_between_two_points_formula(_1st_point, _2nd_point, tab_amount):
    print(f"{tab_amount}2D_point_distance_formula")
    #d = √[(x₂ - x₁)² + (y₂ - y₁)²]
    print(f"{tab_amount}\td = √[(x₂ - x₁)² + (y₂ - y₁)²]")
    print(f"{tab_amount}\td = √[({_2nd_point[0]} - {_1st_point[0]})^2 + ({_2nd_point[1]} - {_1st_point[1]})^2]")
    print(f"{tab_amount}\td = √[({_2nd_point[0] - _1st_point[0]})^2 + ({_2nd_point[1] - _1st_point[1]})^2]")
    print(f"{tab_amount}\td = √[ {math.pow( (_2nd_point[0] - _1st_point[0]),2 )} + {math.pow( (_2nd_point[1] - _1st_point[1]), 2)} ]")
    print(f"{tab_amount}\td = sqrt({math.pow( (_2nd_point[0] - _1st_point[0]),2 ) + math.pow( (_2nd_point[1] - _1st_point[1]), 2)} ]")
    distance = math.sqrt(math.pow( (_2nd_point[0] - _1st_point[0]),2 ) + math.pow( (_2nd_point[1] - _1st_point[1]), 2))
    print(f"{tab_amount}\td = { distance } ")
    return distance



if __name__ == "__main__":

    lab_6_point_A = [3,0]
    lab_6_point_B = [0,4]
    lab_6_point_C = [3,4]

    lab_6_point_D = [4,0]
    lab_6_point_E = [9,0]

    list_of_distances = []

    list_of_distances.append(["A,B", distance_between_two_points_formula(lab_6_point_A, lab_6_point_B, tab_amount="")])
    list_of_distances.append(["A,C", distance_between_two_points_formula(lab_6_point_A, lab_6_point_C, tab_amount="")])
    list_of_distances.append(["A,D", distance_between_two_points_formula(lab_6_point_A, lab_6_point_D, tab_amount="")])
    list_of_distances.append(["A,E", distance_between_two_points_formula(lab_6_point_A, lab_6_point_E, tab_amount="")])

    list_of_distances.append(["B,C", distance_between_two_points_formula(lab_6_point_B, lab_6_point_C, tab_amount="")])
    list_of_distances.append(["B,D", distance_between_two_points_formula(lab_6_point_B, lab_6_point_D, tab_amount="")])
    list_of_distances.append(["B,E", distance_between_two_points_formula(lab_6_point_B, lab_6_point_E, tab_amount="")])

    list_of_distances.append(["C,D", distance_between_two_points_formula(lab_6_point_C, lab_6_point_D, tab_amount="")])
    list_of_distances.append(["C,E", distance_between_two_points_formula(lab_6_point_C, lab_6_point_E, tab_amount="")])

    list_of_distances.append(["D,E", distance_between_two_points_formula(lab_6_point_D, lab_6_point_E, tab_amount="")])

    print()

    print_list(list_of_distances, tab_amount="")

