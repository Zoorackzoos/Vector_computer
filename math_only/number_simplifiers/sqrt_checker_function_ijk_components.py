from math_only.convert_to_divided_by_sqrt import convert_to_divided_by_sqrt


def sqrt_checker_function_ijk_components(i_component, j_component, k_component, tab_amount):
    """
    input = i_component, j_component, k_component
    output = a whole number version of those components

    :param i_component:
    :param j_component:
    :param k_component:
    :param tab_amount:
    :return:
    """
    print(f"{tab_amount}sqrt_checker_function_ijk_components")
    i_component_unsimplified = convert_to_divided_by_sqrt(i_component, tab_amount=tab_amount + '\t')
    j_component_unsimplified = convert_to_divided_by_sqrt(j_component, tab_amount=tab_amount + '\t')
    k_component_unsimplified = convert_to_divided_by_sqrt(k_component, tab_amount=tab_amount + '\t')
    if i_component_unsimplified != None:
        i_component = i_component_unsimplified
    if j_component_unsimplified != None:
        j_component = j_component_unsimplified
    if k_component_unsimplified != None:
        k_component = k_component_unsimplified
    return i_component, j_component, k_component

if __name__ == "__main__":
    print("nothing here bro :(")