from sage.all import Integers, ZZ, euler_phi
from dissect.traits.trait_interface import timeout
from dissect.traits.trait_interface import compute_results
from dissect.utils.custom_curve import CustomCurve

TIMEOUT_DURATION = 30

def a12_curve_function(curve: CustomCurve, l):
    """
    Computes the multiplicative order of l (small prime) modulo curve cardinality and bit length of the index of the
    multiplicative subgroup generated by l Returns a dictionary
    """
    card = curve.cardinality()
    try:
        assert card.gcd(l)==1
        mul_ord = timeout(lambda x: x.multiplicative_order(), [Integers(card)(l)], timeout_duration=TIMEOUT_DURATION)
        euler_phi_card = timeout(lambda x: euler_phi(x[0])*euler_phi(x[1]), [(curve.order(),curve.cofactor())], timeout_duration=TIMEOUT_DURATION*0.5)
        complement_bit_length = ZZ(euler_phi_card / mul_ord).nbits()
    except (TypeError, AssertionError):
        mul_ord = None
        complement_bit_length = None
    curve_results = {"order": mul_ord, "complement_bit_length": complement_bit_length}
    return curve_results


def compute_a12_results(curve_list, desc="", verbose=False):
    compute_results(curve_list, "a12", a12_curve_function, desc=desc, verbose=verbose)
