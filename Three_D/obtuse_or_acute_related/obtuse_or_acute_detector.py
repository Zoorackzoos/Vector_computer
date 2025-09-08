










"""
take 2 vectors
see if they're acute or obtuse
then tell return if what.
or whatever >:-/
"""

from Three_D.dot_product_related.compute_dot_product_3d import dot_product_3d

#made of sin
def obtuse_or_acute_detector(vector_a, vector_b, tab_amount=""):
    print(f"{tab_amount}obtuse_or_acute_detector")
    dot_product_result = dot_product_3d(vector_a, vector_b, tab_amount + "\t")

    if dot_product_result > 0:
        print(f"{tab_amount}Acute Result (< pi/2)")
        return "acute"
    elif dot_product_result < 0:
        print(f"{tab_amount}Obtuse Result (> pi/2)")
        return "obtuse"
    else:
        print(f"{tab_amount}Perpendicular (pi/2)")
        return "perpendicular"












