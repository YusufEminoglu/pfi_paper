"""Transparent baseline modelling utilities."""

from __future__ import annotations

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GroupKFold, KFold


def fit_ols(df: pd.DataFrame, response: str, predictors: list[str]):
    """Fit an OLS model using statsmodels."""
    model_df = df[[response, *predictors]].dropna()
    y = model_df[response]
    x = sm.add_constant(model_df[predictors], has_constant="add")
    return sm.OLS(y, x).fit()


def cross_validated_ols(
    df: pd.DataFrame,
    response: str,
    predictors: list[str],
    group_column: str | None = "hex_id",
    folds: int = 5,
) -> pd.DataFrame:
    """Evaluate an OLS baseline with grouped folds when possible."""
    columns = [response, *predictors]
    if group_column and group_column in df.columns:
        columns.append(group_column)
    model_df = df[columns].dropna().reset_index(drop=True)

    if group_column and group_column in model_df.columns:
        splitter = GroupKFold(n_splits=min(folds, model_df[group_column].nunique()))
        splits = splitter.split(model_df, groups=model_df[group_column])
    else:
        splitter = KFold(n_splits=folds, shuffle=True, random_state=42)
        splits = splitter.split(model_df)

    rows = []
    for fold, (train_idx, test_idx) in enumerate(splits, start=1):
        train = model_df.iloc[train_idx]
        test = model_df.iloc[test_idx]
        fitted = fit_ols(train, response, predictors)
        x_test = sm.add_constant(test[predictors], has_constant="add")
        y_test = test[response]
        y_pred = fitted.predict(x_test)
        rows.append(
            {
                "fold": fold,
                "n_train": len(train),
                "n_test": len(test),
                "r2": r2_score(y_test, y_pred),
                "rmse": float(np.sqrt(mean_squared_error(y_test, y_pred))),
                "mae": mean_absolute_error(y_test, y_pred),
            }
        )
    return pd.DataFrame(rows)

