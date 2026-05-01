"""Validate public processed inputs for the PFI reproducibility workflow."""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from pfi_pipeline.config import BASE_PREDICTORS, COMPONENT_COLUMNS, INTERACTIONS, PROCESSED_DIR
from pfi_pipeline.io import read_table, require_columns


def main() -> None:
    input_path = PROCESSED_DIR / "pfi" / "pfi_merged.csv"
    df = read_table(input_path)
    required = [*COMPONENT_COLUMNS.keys(), *BASE_PREDICTORS]
    for left, right in INTERACTIONS.values():
        required.extend([left, right])
    require_columns(df, sorted(set(required)), "pfi_merged.csv")
    print(f"Input validation passed: {input_path}")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns):,}")


if __name__ == "__main__":
    main()

