from sage.all import factor

from dissect.traits.trait_interface import compute_results
from dissect.utils.custom_curve import CustomCurve


def a22_curve_function(curve: CustomCurve, l):
    """
    Computation factorization of l-th division polynomial
    More precisely, computes a list of tuple [a,b]
    where b is the number of irreducible polynomials of degree a in the factorization (with multiplicity)
    Returns a dictionary
    """
    fact = map(
        lambda x: (
            x[0].degree(), x[1]), factor(
            curve.EC.division_polynomial(l)))
    result = {}
    for deg, ex in fact:
        if deg not in result:
            result[deg] = 0
        result[deg] += ex
    # Converts tuples to lists for json
    result = [list(i) for i in result.items()]
    return {'factorization': result, 'len': len(result)}


def compute_a22_results(curve_list, desc='', verbose=False):
    compute_results(
        curve_list,
        'a22',
        a22_curve_function,
        desc=desc,
        verbose=verbose)
