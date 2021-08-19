import re
from pathlib import Path
from typing import List, Set, Any, Union

from sage.all import ZZ

from dissect.utils.json_handler import load_from_json

ROOT_DIR: Union[Path, Any] = Path(__file__).parent  # This is the project root
CURVE_PATH = "."
CURVE_PATH_SIM = Path(ROOT_DIR, "curves_json_sim")
TRAIT_PATH = Path(ROOT_DIR, "traits")
PARALLEL_RESULTS_PATH = Path(ROOT_DIR, "utils", "parallel", "results")
KOHEL_PATH = Path(ROOT_DIR, "utils", "kohel")
ZVP_PATH = Path(ROOT_DIR, "utils", "zvp")
EFD_PATH = Path(ROOT_DIR, "utils", "efd")
EFD_SHORTW_PROJECTIVE_ADDITION_PATH = Path(EFD_PATH, "shortw", "projective", "addition")
EFD_SHORTW_PROJECTIVE_ADDITION_FORMULAE = [
    f for f in EFD_SHORTW_PROJECTIVE_ADDITION_PATH.iterdir() if f.suffix == ".op3"
]
EFD_SHORTW_PROJECTIVE_MINUS3_ADDITION_PATH = Path(
    EFD_PATH, "shortw", "projective-3", "addition"
)
EFD_SHORTW_PROJECTIVE_MINUS3_ADDITION_FORMULAE = [
    f
    for f in EFD_SHORTW_PROJECTIVE_MINUS3_ADDITION_PATH.iterdir()
    if f.suffix == ".op3"
]
UNROLLED_ADDITION_FORMULAE_PATH = Path(EFD_PATH, "unrolled_formulae", "addition")
UNROLLED_ADDITION_FORMULAE_MODULE_PATH = "dissect.utils.efd.unrolled_formulae.addition"
UNROLLED_ADDITION_FORMULAE = [
    f for f in UNROLLED_ADDITION_FORMULAE_PATH.iterdir() if f.suffix == ".py"
]
X962_PATH = Path(ROOT_DIR, "utils", "parallel", "x962")
SECG_PATH = Path(ROOT_DIR, "utils", "parallel", "secg")
BRAINPOOL_PATH = Path(ROOT_DIR, "utils", "parallel", "brainpool")
STANDARDS = ["brainpool, x962"]
TRAIT_MODULE_PATH: str = "dissect.traits"
TRAIT_NAME_CONDITION = r"[ais][0-9][0-9]"
TRAIT_NAMES: List[str] = sorted([
    f.name
    for f in TRAIT_PATH.iterdir()
    if f.is_dir() and re.search(TRAIT_NAME_CONDITION, f.name)
])

STD_BITLENGTHS = set()
STD_COFACTORS: Set[ZZ] = set()
STD_CURVE_NAMES = []
STD_CURVE_DICT = {}
STD_CURVE_COUNT = len(STD_CURVE_NAMES)
STD_COFACTORS = sorted(STD_COFACTORS)
STD_SOURCES = ["anssi","bls","bn","brainpool","gost","mnt","nist","nums","oakley","oscaa","other","secg","wtls","x962","x963"]
STD_BITLENGTHS = sorted(STD_BITLENGTHS)

# SIM_BITLENGTHS = list(map(ZZ, [d.name for d in Path(CURVE_PATH_SIM, "x962_sim").iterdir() if d.is_dir()]))
# SIM_COFACTORS = set()
# for d in Path(CURVE_PATH_SIM, "x962_sim").iterdir():
#     if d.is_dir():
#         for f in d.iterdir():
#             curves = load_from_json(f)["curves"]
#             for curve in curves:
#                 SIM_COFACTORS.add(ZZ(curve["cofactor"]))
# SIM_COFACTORS = sorted(SIM_COFACTORS)
ALL_CURVE_COUNT = 217396
SIM_CURVE_COUNT = ALL_CURVE_COUNT - STD_CURVE_COUNT
SIM_BITLENGTHS = [128, 160, 192, 224, 256]
SIM_COFACTORS = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
]
ALL_COFACTORS = sorted(set(STD_COFACTORS + SIM_COFACTORS))

TRAIT_DESCRIPTIONS = dict(
    sorted(load_from_json(Path(TRAIT_PATH, "trait_descriptions")).items(), key=lambda item: item[0]))
