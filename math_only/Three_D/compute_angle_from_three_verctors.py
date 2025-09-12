from Three_D.dot_product_related.compute_dot_product_3d import dot_product_3d
from math_only.Three_D.combine_vectors_3d import combine_vectors_3d
from math_only.Three_D.ABS_for_vertex_aka_distance_formula import ABS_for_vectors_AKA_distance_formula

def compute_angle_from_three_vertexes(vertex_a, vertex_b,vertex_c, tab_amount):
    #   A PRIMARY
    vertex_ab = combine_vectors_3d(vector_a=vertex_a, vector_b=vertex_b, tab_amount="\t")
    vertex_ab_ABSified = ABS_for_vectors_AKA_distance_formula(vertex_ab, tab_amount=tab_amount + '\t')

    vertex_ac = combine_vectors_3d(vector_a=vertex_a, vector_b=vertex_c, tab_amount="\t")
    vertex_ac_ABSified = ABS_for_vectors_AKA_distance_formula(vertex_ac, tab_amount=tab_amount + '\t')

    ab_ac_dot_product = dot_product_3d(vertex_ab, vertex_ac, tab_amount + '\t')
    conbined_ab_ac_ABS_nums = vertex_ab_ABSified * vertex_ac_ABSified
    #ab_ac_arc_cos_input = ab_ac_dot_product / math.sqrt(conbined_ab_ac_ABS_nums)


    #   B PRIMARY
    vertex_ba = combine_vectors_3d(vector_a=vertex_b, vector_b=vertex_a, tab_amount="\t")
    vertex_ba_ABSified = ABS_for_vectors_AKA_distance_formula(vertex_ba, tab_amount=tab_amount + '\t')

    vertex_bc = combine_vectors_3d(vector_a=vertex_b, vector_b=vertex_c, tab_amount="\t")
    vertex_bc_ABSified = ABS_for_vectors_AKA_distance_formula(vertex_bc, tab_amount=tab_amount + '\t')

    ba_bc_dot_product = dot_product_3d(vertex_ba, vertex_bc, tab_amount + '\t')
    conbined_ba_bc_nums = vertex_ba_ABSified * vertex_bc_ABSified

    #   C PRIMARY
    vertex_ca = combine_vectors_3d(vector_a=vertex_c, vector_b=vertex_a, tab_amount="\t")
    vertex_ca_ABSified = ABS_for_vectors_AKA_distance_formula(vertex_ca, tab_amount=tab_amount + '\t')

    vertex_cb = combine_vectors_3d(vector_a=vertex_c, vector_b=vertex_b, tab_amount="\t")
    vertex_cb_ABSified = ABS_for_vectors_AKA_distance_formula(vertex_cb, tab_amount=tab_amount + '\t')

    ca_cb_dot_product = dot_product_3d(vertex_ca, vertex_cb, tab_amount + '\t')
    conbined_ca_cb_ABSified_nums = vertex_ca_ABSified * vertex_cb_ABSified

    print(f"{tab_amount}\t'A' PRIMARY")
    print(f"{tab_amount}\t\t{ab_ac_dot_product}")
    print(f"{tab_amount}\t\t/////")
    print(f"{tab_amount}\t\tsqrt({conbined_ab_ac_ABS_nums})")
    print()
    print(f"{tab_amount}\t'B' PRIMARY")
    print(f"{tab_amount}\t\t{ba_bc_dot_product}")
    print(f"{tab_amount}\t\t/////")
    print(f"{tab_amount}\t\tsqrt({conbined_ba_bc_nums})")
    print()
    print(f"{tab_amount}\t'C' PRIMARY")
    print(f"{tab_amount}\t\t{ca_cb_dot_product}")
    print(f"{tab_amount}\t\t/////")
    print(f"{tab_amount}\t\tsqrt({conbined_ca_cb_ABSified_nums})")

if __name__ == '__main__':
    D = [1,1,1]
    E = [1,-4,2]
    F = [-6,2,5]

    compute_angle_from_three_vertexes(vertex_a=D, vertex_b=E, vertex_c=F, tab_amount='')

