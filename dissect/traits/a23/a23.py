from sage.all import kronecker, ZZ

from dissect.traits.trait_interface import compute_results
from dissect.utils.custom_curve import CustomCurve


def a23_curve_function(curve: CustomCurve, l):
    """
    Computes the depth of volcano and the degree of the crater subgraph containing E
    Returns a dictionary (keys: 'crater_degree', 'depth')
    """
    D = curve.extended_frobenius_disc()
    curve_results = {}
    if l != 2:
        curve_results["crater_degree"] = kronecker(D, l) + 1
        curve_results["depth"] = ZZ.valuation(l)(D) // 2
    else:
        e = ZZ.valuation(2)(D)
        if e % 2 == 0:
            d = D // (2 ** e)
            if d % 4 != 1:
                curve_results["crater_degree"] = 1
                curve_results["depth"] = e // 2 - 1
            else:
                curve_results["crater_degree"] = kronecker(d, l) + 1
                curve_results["depth"] = e // 2
        else:
            curve_results["crater_degree"] = 1
            curve_results["depth"] = e // 2 - 1
    return curve_results


def compute_a23_results(curve_list, desc="", verbose=False):
    compute_results(curve_list, "a23", a23_curve_function, desc=desc, verbose=verbose)
