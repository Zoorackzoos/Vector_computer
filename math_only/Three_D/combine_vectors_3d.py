def combine_vectors_3d( vector_a, vector_b, tab_amount):
    """
    DE = E - D = ....

    i asked what thhis is called to Du
    bruh didn't know wtf i was talking about
    "what do i call it?"
        "which one is left?"
    "huh?"
    gee Thanks Du.
        moron...

    :param vertex_1:
    :param vertex_2:
    :return:
    """
    print(f"{tab_amount}conbine_verticies_3d")
    print(f"{tab_amount}\tvertex_b_x - vertex_a_x, vertex_b_y - vertex_a_y, vertex_b_z - vertex_a_z")
    print(f"{tab_amount}\t{vector_b[0]} - {vector_a[0]}, {vector_b[1]} - {vector_a[1]}, {vector_b[2]} - {vector_a[2]}")

    temp_x = vector_b[0] - vector_a[0]
    temp_y = vector_b[1] - vector_a[1]
    temp_z = vector_b[2] - vector_a[2]

    print(f"{tab_amount}\t{temp_x}, {temp_y}, {temp_z}")

    temp_list = [temp_x, temp_y, temp_z]
    return temp_list

if __name__ == "__main__":

    D = [1,2,3]
    E = [4,5,6]

    combine_vectors_3d(vector_a=D, vector_b=E, tab_amount="")