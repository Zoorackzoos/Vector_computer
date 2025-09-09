import math


def abs_for_vertex(vertex,tab_amount):
    print(f"{tab_amount}abs_for_vertex")
    print(f"{tab_amount}\tsqrt(x^2 + y^2 + z^2)")
    print(f"{tab_amount}\tsqrt({vertex[0]}^2 + {vertex[1]}^2 + {vertex[2]}^2)")
    print(f"{tab_amount}\tsqrt({math.pow(vertex[0],2)} + {math.pow(vertex[1],2)} + {math.pow(vertex[2],2)})")
    print(f"{tab_amount}\tsqrt({math.pow(vertex[0],2)+math.pow(vertex[1],2)+math.pow(vertex[2],2)})")
    output_num = math.pow(vertex[0],2) + math.pow(vertex[1],2) + math.pow(vertex[2],2)
    print(f"{tab_amount}\t{math.sqrt(output_num)}")
    return output_num

if __name__ == "__main__":
    vertex_var = [-4,1,-10]
    vertex_var__1_4_4 = [2,-2,-4]
    vertex_var__1_4_7_force = [0,5,2]
    vertex_var__1_4_8 = [9,0,-9]

    vertex_in_question = vertex_var__1_4_8

    print( abs_for_vertex(vertex=vertex_in_question,tab_amount="\t"))