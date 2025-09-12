










from math_only.Three_D.area_of_triangle_with_three_vector_points import area_of_triangle_with_three_vector_points_steps_1_2

def find_equation_for_plane_of_three_vectors(vector_a, vector_b, vector_c, tab_amount):
    print(f"{tab_amount}find_equation_for_plane_of_three_vectors")
    step_1_2_vector = area_of_triangle_with_three_vector_points_steps_1_2(vector_a=vector_a, vector_b=vector_b, vector_c=vector_c, tab_amount=tab_amount+'\t')
    print(f"{tab_amount}\tstep_1_2_vector = {step_1_2_vector}")

    halfed_vector = []
    halfed_vector.append( (step_1_2_vector[0] / 2) )
    halfed_vector.append( (step_1_2_vector[1] / 2) )
    halfed_vector.append( (step_1_2_vector[2] / 2) )

    print(f"{tab_amount}\tstep_1_2_vector[0] / 2 = {halfed_vector[0]}")
    print(f"{tab_amount}\tstep_1_2_vector[1] / 2 = {halfed_vector[1]}")
    print(f"{tab_amount}\tstep_1_2_vector[2] / 2 = {halfed_vector[2]}")

    print()

    print(f"{tab_amount}\ta(x - x_0) + b(y - y_0) + c(z - z_0)")
    print(f"{tab_amount}\thalfed_vector\t = \ta, b, c \t= \t{halfed_vector}")
    print(f"{tab_amount}\tvector_a\t = \tx_0, y_0, z_0 \t= \t{vector_a}")
    print()
    print(f"{tab_amount}\t "
          f"{halfed_vector[0]}(x - {vector_a[0]}) + "
          f"{halfed_vector[1]}(y - {vector_a[1]}) + "
          f"{halfed_vector[2]}(z - {vector_a[2]})")

    constant_x = vector_a[0] * halfed_vector[0]
    constant_y = vector_a[1] * halfed_vector[1]
    constant_z = vector_a[2] * halfed_vector[2]

    print(f"{tab_amount}\t "
          f"{halfed_vector[0]}x - {constant_x} + "
          f"{halfed_vector[1]}y - {constant_y} + "
          f"{halfed_vector[2]}z - {constant_z}")

    constant_total = constant_x + constant_y + constant_z

    return_value_string = f"{halfed_vector[0]}x + {halfed_vector[1]}y + {halfed_vector[2]}z + {constant_total}"

    print(f"{tab_amount}\t {return_value_string}")
    print(f"{tab_amount}\t\t you're going to have to do some algebra now becuas ei don't know how to do algebra as a computer sorry bro")
    print(f"{tab_amount}\t\t i'm going to return this as a String")
    return return_value_string

if __name__ == "__main__":
    P = [0, 1, 0]
    Q = [1, -1, 1]
    R = [-1, 1, -1]

    find_equation_for_plane_of_three_vectors(P, Q, R, tab_amount='')














