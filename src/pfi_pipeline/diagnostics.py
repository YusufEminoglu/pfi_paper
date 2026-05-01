"""Model-diagnostic helpers for the public reproducibility package."""

from __future__ import annotations

import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor


def variance_inflation_table(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Calculate VIF values for numeric predictor columns."""
    x = df[columns].apply(pd.to_numeric, errors="coerce").dropna()
    rows = []
    for index, column in enumerate(columns):
        rows.append(
            {
                "variable": column,
                "vif": float(variance_inflation_factor(x.to_numpy(), index)),
            }
        )
    return pd.DataFrame(rows).sort_values("vif", ascending=False)


def descriptive_summary(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Return a compact descriptive summary for selected variables."""
    summary = df[columns].describe(percentiles=[0.25, 0.5, 0.75]).T
    return summary.reset_index(names="variable")

