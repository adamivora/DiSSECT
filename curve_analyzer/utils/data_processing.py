from typing import Dict, Any

import pandas as pd

import curve_analyzer.utils.database_handler as database
from curve_analyzer.definitions import STD_CURVE_DICT

db = None


def load_trait(trait: str, params: Dict[str, Any] = None, curve: str = None) -> pd.DataFrame:
    global db
    if not db:
        db = database.connect()

    return pd.DataFrame(database.get_trait_results(db, trait))


def load_curves(filters: Any = {}) -> pd.DataFrame:
    global db
    if not db:
        db = database.connect()

    def project(record: Dict[str, Any]):
        projection = {}
        projection["curve"] = record["name"]
        projection["cofactor"] = int(record["cofactor"], base=16) if isinstance(record["cofactor"], str) else int(record["cofactor"])
        projection["bitlength"] = record["field"]["bits"]
        projection["simulated"] = record["simulated"]
        return projection

    df = pd.DataFrame(map(project, database.get_curves(db, filters, raw=True)))
    return df


def filter_df(df, bitlengths, sources, max_cofactor=1):
    # Remove entries with NaN values
    df = df.dropna()
    allowed_curves = []
    for source in sources:
        try:
            allowed_curves += STD_CURVE_DICT[source]
        except KeyError:
            pass
    if "sim" in sources:
        if not "std" in sources:
            df = df[df.curve.isin(allowed_curves) | df.simulated]
    elif "std" in sources:
        df = df[~df.simulated]
    else:
        df = df[df.curve.isin(allowed_curves) & ~df.simulated]
    df = df[df["bitlength"].isin(bitlengths)]
    df = df[df["cofactor"] <= max_cofactor]
    return df
