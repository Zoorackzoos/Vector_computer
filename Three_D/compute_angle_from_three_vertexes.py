from Three_D.dot_product_related.compute_dot_product_3d import dot_product_3d
from Three_D.combine_verticies_3d import conbine_verticies_3d
from Three_D.abs_for_vertex import abs_for_vertex

def compute_angle_from_three_vertexes(vertex_a, vertex_b,vertex_c, tab_amount):
    #   A PRIMARY
    vertex_ab = conbine_verticies_3d(vertex_a=vertex_a, vertex_b=vertex_b, tab_amount="\t")
    vertex_ab_ABSified = abs_for_vertex(vertex_ab, tab_amount=tab_amount+'\t')

    vertex_ac = conbine_verticies_3d(vertex_a=vertex_a, vertex_b=vertex_c, tab_amount="\t")
    vertex_ac_ABSified = abs_for_vertex(vertex_ac, tab_amount=tab_amount+'\t')

    ab_ac_dot_product = dot_product_3d(vertex_ab, vertex_ac, tab_amount + '\t')
    conbined_ab_ac_ABS_nums = vertex_ab_ABSified * vertex_ac_ABSified
    #ab_ac_arc_cos_input = ab_ac_dot_product / math.sqrt(conbined_ab_ac_ABS_nums)


    #   B PRIMARY
    vertex_ba = conbine_verticies_3d(vertex_a=vertex_b, vertex_b=vertex_a, tab_amount="\t")
    vertex_ba_ABSified = abs_for_vertex(vertex_ba, tab_amount=tab_amount+'\t')

    vertex_bc = conbine_verticies_3d(vertex_a=vertex_b, vertex_b=vertex_c, tab_amount="\t")
    vertex_bc_ABSified = abs_for_vertex(vertex_bc, tab_amount=tab_amount+'\t')

    ba_bc_dot_product = dot_product_3d(vertex_ba, vertex_bc, tab_amount + '\t')
    conbined_ba_bc_nums = vertex_ba_ABSified * vertex_bc_ABSified

    #   C PRIMARY
    vertex_ca = conbine_verticies_3d(vertex_a=vertex_c, vertex_b=vertex_a, tab_amount="\t")
    vertex_ca_ABSified = abs_for_vertex(vertex_ca, tab_amount=tab_amount+'\t')

    vertex_cb = conbine_verticies_3d(vertex_a=vertex_c, vertex_b=vertex_b, tab_amount="\t")
    vertex_cb_ABSified = abs_for_vertex(vertex_cb, tab_amount=tab_amount+'\t')

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

