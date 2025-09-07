import math


def abs_for_vertex(vertex,tab_amount):
    print(f"{tab_amount}abs_for_vertex")
    print(f"{tab_amount}\tsqrt({math.pow(vertex[0],2)} + {math.pow(vertex[1],2)} + {math.pow(vertex[2],2)})")
    print(f"{tab_amount}\tsqrt({math.pow(vertex[0],2)+math.pow(vertex[1],2)+math.pow(vertex[2],2)})")
    output_num = math.pow(vertex[0],2) + math.pow(vertex[1],2) + math.pow(vertex[2],2)
    print(f"{tab_amount}\t{math.sqrt(output_num)}")
    return output_num

if __name__ == "__main__":
    vertex_var = [-4,1,-10]
    print( abs_for_vertex(vertex=vertex_var,tab_amount="\t"))