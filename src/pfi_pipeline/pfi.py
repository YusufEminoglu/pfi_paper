"""Pedestrian Friction Index construction utilities."""

from __future__ import annotations

import numpy as np
import pandas as pd


def zscore(series: pd.Series) -> pd.Series:
    """Return a population-standardized z score."""
    values = pd.to_numeric(series, errors="coerce")
    std = values.std(ddof=0)
    if std == 0 or np.isnan(std):
        return values * np.nan
    return (values - values.mean()) / std


def compute_pfi(
    df: pd.DataFrame,
    pcs_column: str = "PCS_z",
    tfs_column: str = "TFS_z",
    pcs_weight: float = 0.597,
    tfs_weight: float = 0.403,
) -> pd.Series:
    """Compute PFI from standardized physical and thermal components."""
    if pcs_column not in df.columns or tfs_column not in df.columns:
        raise ValueError(f"PFI requires '{pcs_column}' and '{tfs_column}'.")
    return (pcs_weight * df[pcs_column]) + (tfs_weight * df[tfs_column])


def add_interactions(
    df: pd.DataFrame,
    interactions: dict[str, tuple[str, str]],
) -> pd.DataFrame:
    """Add pairwise interaction terms to a model matrix."""
    result = df.copy()
    for output_column, (left, right) in interactions.items():
        if left not in result.columns or right not in result.columns:
            raise ValueError(
                f"Interaction '{output_column}' requires missing columns: {left}, {right}"
            )
        result[output_column] = result[left] * result[right]
    return result

