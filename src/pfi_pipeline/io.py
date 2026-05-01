"""Input and output helpers for tabular reproducibility files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def read_table(path: str | Path) -> pd.DataFrame:
    """Read a CSV table with a clear error message."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Required input file was not found: {path}")
    return pd.read_csv(path)


def write_table(df: pd.DataFrame, path: str | Path) -> None:
    """Write a CSV table and create parent directories when needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def require_columns(df: pd.DataFrame, columns: list[str], table_name: str) -> None:
    """Raise a useful error if required columns are absent."""
    missing = [column for column in columns if column not in df.columns]
    if missing:
        missing_text = ", ".join(missing)
        raise ValueError(f"{table_name} is missing required columns: {missing_text}")

