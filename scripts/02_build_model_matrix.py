"""Build the public analytical model matrix from processed node metrics."""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from pfi_pipeline.config import (
    BASE_PREDICTORS,
    IDENTIFIER_COLUMNS,
    INTERACTIONS,
    OUTPUT_DIR,
    PROCESSED_DIR,
    RESPONSE_COLUMN,
)
from pfi_pipeline.io import read_table, require_columns, write_table
from pfi_pipeline.pfi import add_interactions, compute_pfi


def main() -> None:
    input_path = PROCESSED_DIR / "pfi" / "pfi_merged.csv"
    df = read_table(input_path)

    if RESPONSE_COLUMN not in df.columns:
        require_columns(df, ["PCS_z", "TFS_z"], "pfi_merged.csv")
        df[RESPONSE_COLUMN] = compute_pfi(df)

    require_columns(df, [RESPONSE_COLUMN, *BASE_PREDICTORS], "pfi_merged.csv")
    df = add_interactions(df, INTERACTIONS)

    available_ids = [column for column in IDENTIFIER_COLUMNS if column in df.columns]
    output_columns = [
        *available_ids,
        RESPONSE_COLUMN,
        *BASE_PREDICTORS,
        *INTERACTIONS.keys(),
    ]
    model_matrix = df[output_columns].copy()
    output_path = OUTPUT_DIR / "model_matrix.csv"
    write_table(model_matrix, output_path)
    print(f"Model matrix written: {output_path}")
    print(f"Rows: {len(model_matrix):,}")
    print(f"Predictors: {len(BASE_PREDICTORS) + len(INTERACTIONS):,}")


if __name__ == "__main__":
    main()

