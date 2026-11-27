# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas>=2.2", "numpy", "scikit-learn>=1.5"]
# ///
"""Validation action V-03: how good is a simple lookup table (Option B)
compared with the Week 9 model (Option C) and the goal rule (baseline)?

Run:  uv run analysis/option_b_lookup_check.py <path to ks-projects-201801.csv>

The CSV is the Kaggle dataset "Kickstarter Projects" (kemical), licence
CC BY-NC-SA 4.0. It is NOT stored in this repository; download it yourself.
Cleaning and the train/test split copy the Week 9 project
(crsbln/ds-ml-project-template, src/kickstarter): same rows, same 80/20
stratified split with random_state 42, so the numbers are comparable.
Writes analysis/option_b_lookup_results.json next to this script.
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import brier_score_loss, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder

RANDOM_STATE = 42
GOAL_BINS = [0, 1_000, 2_500, 5_000, 10_000, 25_000, 50_000, 100_000, np.inf]
LEN_BINS = [0, 14, 29, 30, 44, 59, 60, 92]
CAT = ["category", "country"]
NUM = ["log_goal", "duration_days", "launch_month", "launch_weekday",
       "name_length", "name_words"]
TUNED = dict(learning_rate=0.05, max_iter=400, max_leaf_nodes=31,
             min_samples_leaf=100, l2_regularization=1.0)
STATUS_TAG = r"\s*\((?:canceled|suspended)\)"
CUR = {"USD": "US", "GBP": "GB", "AUD": "AU", "CAD": "CA", "DKK": "DK",
       "NOK": "NO", "SEK": "SE", "EUR": "EU"}


def clean(raw: pd.DataFrame) -> pd.DataFrame:
    """Same steps as the Week 9 project (src/kickstarter/data.py)."""
    p = raw[~raw["state"].isin(["live", "undefined"])].copy()
    p["success"] = (p["state"] == "successful").astype(int)
    p["launched"] = pd.to_datetime(p["launched"])
    p["deadline"] = pd.to_datetime(p["deadline"])
    p["duration_days"] = (p["deadline"] - p["launched"].dt.normalize()).dt.days
    p = p[p["launched"].dt.year != 1970].copy()
    bad = p["country"] == 'N,0"'
    p.loc[bad, "country"] = p.loc[bad, "currency"].map(CUR).fillna("Unknown")
    p["name"] = (p["name"].str.replace(STATUS_TAG, "", regex=True, case=False)
                 .str.strip().fillna(""))
    p["launch_year"] = p["launched"].dt.year
    p["launch_month"] = p["launched"].dt.month
    p["launch_weekday"] = p["launched"].dt.day_of_week
    p["log_goal"] = np.log1p(p["usd_goal_real"])
    p["name_length"] = p["name"].str.len()
    p["name_words"] = p["name"].str.split().str.len()
    p["goal_band"] = pd.cut(p["usd_goal_real"], GOAL_BINS, include_lowest=True)
    p["len_group"] = pd.cut(p["duration_days"], LEN_BINS, include_lowest=True)
    return p


def lookup(train: pd.DataFrame, test: pd.DataFrame, keys, k=50.0):
    """Funding rate per cell of the table, learned on train only.

    Small cells are pulled towards the overall rate (k = how many
    campaigns a cell needs before its own rate counts half).
    """
    overall = train["success"].mean()
    g = train.groupby(keys, observed=True)["success"].agg(["sum", "count"])
    g["rate"] = (g["sum"] + k * overall) / (g["count"] + k)
    rate = test.join(g["rate"], on=keys)["rate"].fillna(overall)
    return rate.to_numpy(), len(g)


def model(train: pd.DataFrame, test: pd.DataFrame):
    pre = ColumnTransformer([
        ("c", OrdinalEncoder(handle_unknown="use_encoded_value",
                             unknown_value=-1, encoded_missing_value=-1), CAT),
        ("n", "passthrough", NUM)])
    gb = HistGradientBoostingClassifier(
        categorical_features=[True, True] + [False] * len(NUM),
        random_state=RANDOM_STATE, **TUNED)
    pipe = Pipeline([("p", pre), ("m", gb)]).fit(train[CAT + NUM],
                                                 train["success"])
    return pipe.predict_proba(test[CAT + NUM])[:, 1]


def score(y, proba) -> dict:
    return {"roc_auc": round(float(roc_auc_score(y, proba)), 3),
            "brier": round(float(brier_score_loss(y, proba)), 3)}


def evaluate(train, test) -> dict:
    y = test["success"]
    out = {"train_rows": len(train), "test_rows": len(test)}
    rule = (test["log_goal"] < train["log_goal"].median()).astype(int)
    out["C0 goal rule (yes/no)"] = {
        "roc_auc": round(float(roc_auc_score(y, rule)), 3)}
    # The same rule as a ranking: the smaller the goal, the higher the rank
    out["C0 goal as ranking"] = {
        "roc_auc": round(float(roc_auc_score(y, -test["log_goal"])), 3)}
    tables = {
        "B1 category (15)": ["main_category"],
        "B2 category x goal band": ["main_category", "goal_band"],
        "B3 category x goal x length": ["main_category", "goal_band",
                                        "len_group"],
        "B4 subcategory x goal band": ["category", "goal_band"],
    }
    for name, keys in tables.items():
        proba, cells = lookup(train, test, keys)
        out[name] = score(y, proba) | {"cells": cells}
    # Reference: say "36 %" (the training average) for every campaign
    flat = np.full(len(test), train["success"].mean())
    out["A0 same number for everyone"] = {
        "brier": round(float(brier_score_loss(y, flat)), 3)}
    # Sensitivity: does the untuned smoothing k change the 120-cell table?
    out["B2 smoothing sensitivity (k: roc_auc)"] = {
        str(k): round(float(roc_auc_score(
            y, lookup(train, test, ["main_category", "goal_band"], k)[0])), 3)
        for k in (0, 10, 50, 200)}
    out["C model (Week 9 settings)"] = score(y, model(train, test))
    return out


def main():
    csv = Path(sys.argv[1])
    p = clean(pd.read_csv(csv))
    res = {"rows": len(p), "funded_share": round(float(p["success"].mean()), 3)}
    tr, te = train_test_split(p, test_size=0.20, stratify=p["success"],
                              random_state=RANDOM_STATE)
    res["random_split"] = evaluate(tr, te)
    early = p["launch_year"] < 2016
    res["time_split_train_before_2016"] = evaluate(p[early], p[~early])
    out = Path(__file__).with_name("option_b_lookup_results.json")
    out.write_text(json.dumps(res, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
