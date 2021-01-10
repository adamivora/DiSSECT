import json

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import DuplicateKeyError
from curve_analyzer.utils.custom_curve import CustomCurve
from sage.all import Integer
from typing import Optional, Tuple, Iterable, Dict, Any


def connect(database: Optional[str] = None) -> Database:
    client = MongoClient(database)
    return client["dissect"]


def create_curves_index(db: Database) -> None:
    db["curves"].create_index([("name", 1)], unique=True)


def create_trait_index(db: Database, trait: str) -> None:
    db[f"trait_{trait}"].create_index([("curve", 1), ("params", 1)], unique=True)


def upload_curves(db: Database, path: str) -> Tuple[int, int]:
    try:
        with open(path, "r") as f:
            curves = json.load(f)

        if not isinstance(curves, list):  # inconsistency between simulated and standard format
            curves = curves["curves"]
    except Exception:  # invalid format
        return 0, 0

    for curve in curves:
        curve["simulated"] = True if "sim" in curve["category"] else False
        if isinstance(curve["order"], int):
            curve["order"] = hex(curve["order"])

    success = 0
    for curve in curves:
        try:
            if db["curves"].insert_one(curve):
                success += 1
        except DuplicateKeyError:
            pass

    return success, len(curves)


def upload_results(db: Database, trait_name: str, path: str) -> Tuple[int, int]:
    try:
        with open(path, "r") as f:
            results = json.load(f)
    except Exception:  # invalid format
        return 0, 0

    success = 0
    total = 0
    for curve, result in results.items():
        for params, values in result.items():
            params = params.replace("'", '"')
            total += 1
            record = {
                "curve": curve,
                "params": json.loads(params),
                "result": _cast_sage_types(values)
            }
            try:
                if db[f"trait_{trait_name}"].insert_one(record):
                    success += 1
            except:
                pass
    return success, total


def get_curves(db: Database, filters: Any) -> Iterable[CustomCurve]:
    curve_filter: Dict[str, Any] = {}

    # Curve type filter
    if filters.curve_type == "sim":
        curve_filter["simulated"] = True
    elif filters.curve_type == "std":
        curve_filter["simulated"] = False
    elif filters.curve_type == "sample":
        curve_filter["simulated"] = False
        curve_filter["name"] = { "$in": ["secp112r1", "secp192r1", "secp256r1"] }
    elif filters.curve_type != "all":
        curve_filter["name"] = filters.curve_type

    # Bit-length filter
    curve_filter["field.bits"] = { "$lte": filters.order_bound }

    # Cofactor filter
    # TODO discuss if (allowed_cofactor == None => match_any) is ok
    if filters.allowed_cofactors:
        curve_filter["cofactor"] = { "$in": list(map(int, filters.allowed_cofactors)) }

    # Cursor tends to timeout -> collect the results first (memory heavy)
    curves = list(db.curves.find(curve_filter))
    # Alternative solution, but it needs to be freed (curves.close() or with construct)
    # curves = db.curves.find(curve_filter, no_cursor_timeout=True)

    return map(CustomCurve, curves)


# TODO this should be IMO handled by the traits - after finishing computation transform Sage values into Python values
def _cast_sage_types(result: Any) -> Any:
    if isinstance(result, int):
        return result if abs(result) < 2 ** 63 else hex(result)

    if isinstance(result, Integer):
        return _cast_sage_types(int(result))

    if isinstance(result, dict):
        for key, value in result.items():
            result[key] = _cast_sage_types(value)
    elif isinstance(result, list):
        for idx, value in enumerate(result):
            result[idx] = _cast_sage_types(value)

    return result


def store_trait_result(db: Database, curve: CustomCurve, trait: str, params: Dict[str, Any], result: Dict[str, Any]) -> bool:
    trait_result = { "curve": curve.name }
    trait_result["params"] = _cast_sage_types(params)
    trait_result["result"] = _cast_sage_types(result)
    try:
        return db[f"trait_{trait}"].insert_one(trait_result).acknowledged
    except DuplicateKeyError:
        return False


def is_solved(db: Database, curve: CustomCurve, trait: str, params: Dict[str, Any]) -> bool:
    trait_result = { "curve": curve.name }
    trait_result["params"] = _cast_sage_types(params)
    return db[f"trait_{trait}"].find_one(trait_result) is not None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3 or not sys.argv[1] in ("curves", "results"):
        print(f"USAGE: python {sys.argv[0]} curves [database_uri] <curve_files...>", file=sys.stderr)
        print(f"   OR: python {sys.argv[0]} results [database_uri] <trait_name> <results_file>", file=sys.stderr)
        sys.exit(1)

    database_uri = "mongodb://localhost:27017/"
    args = sys.argv[2:]
    for idx, arg in enumerate(args):
        if "mongodb://" in arg:
            database_uri = arg
            del args[idx]
            break

    print(f"Connecting to database {database_uri}")
    db = connect(database_uri)

    if sys.argv[1] == "curves":
        for curves_file in args:
            print(f"Loading curves from file {curves_file}")
            create_curves_index(db)
            uploaded, total = upload_curves(db, curves_file)
            print(f"Successfully uploaded {uploaded} out of {total}")
    else:
        trait_name = args[0]
        results_file = args[1]
        print(f"Loading trait {trait_name} results from file {results_file}")
        create_trait_index(db, trait_name)
        uploaded, total = upload_results(db, trait_name, results_file)
        print(f"Successfully uploaded {uploaded} out of {total}")
