from sage.all import ZZ, sqrt

from dissect.utils.utils import Factorization
from dissect.traits.trait_interface import compute_results
from dissect.utils.custom_curve import CustomCurve

TRAIT_TIMEOUT = 60


def a06_curve_function(curve: CustomCurve, deg):
    """returns the factorization of the D_deg/D_1, where D_deg is the discriminant over the deg-th relative
    extension"""
    curve_results = {}
    disc_base = curve.extended_frobenius_disc()
    disc_ext =  curve.extended_frobenius_disc(deg)
    ratio_sqrt = ZZ(sqrt(disc_ext / disc_base))
    curve_results["ratio_sqrt"] = ratio_sqrt
    curve_results["factorization"] = Factorization(ratio_sqrt, timeout_duration=TRAIT_TIMEOUT).factorization()
    return curve_results


def compute_a06_results(curve_list, desc="", verbose=False):
    compute_results(curve_list, "a06", a06_curve_function, desc=desc, verbose=verbose)
