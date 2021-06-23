from sage.all import ZZ, sqrt

import dissect.traits.trait_utils as tu
from dissect.traits.trait_interface import compute_results
from dissect.traits.trait_utils import ext_disc
from dissect.utils.custom_curve import CustomCurve

TRAIT_TIMEOUT = 20


def a02_curve_function(curve: CustomCurve):
    """
    Computation of d_K (cm_disc), v (max_conductor) and factorization of D where D=t^2-4q = v^2*d_K
    Returns a dictionary (keys: 'cm_disc', 'factorization', 'max_conductor')
    """
    D = ext_disc(curve, deg=1)
    if curve.cm_discriminant is not None:
        cm_disc = curve.cm_discriminant
        max_conductor = ZZ(sqrt(D / cm_disc))
        conductor_fact = tu.factorization(max_conductor)
        if isinstance(conductor_fact, str):
            return {"cm_disc": conductor_fact, "factorization": conductor_fact, "max_conductor": conductor_fact}
        cm_fact = tu.factorization(cm_disc)
        if isinstance(cm_fact, str):
            return {"cm_disc": conductor_fact, "factorization": conductor_fact, "max_conductor": conductor_fact}
        F = sorted(conductor_fact+conductor_fact+cm_fact)
    else:
        res = tu.squarefree_and_factorization(D)
        if isinstance(res, str):
            return {"cm_disc": res, "factorization": res, "max_conductor": res}
        d, F = res
        cm_disc = d
        if d % 4 != 1:
            cm_disc *= 4
        max_conductor = ZZ(sqrt(D / cm_disc))

    curve_results = {"cm_disc": cm_disc, "factorization": F, "max_conductor": max_conductor}
    return curve_results


def compute_a02_results(curve_list, desc="", verbose=False):
    compute_results(curve_list, "a02", a02_curve_function, desc=desc, verbose=verbose)
