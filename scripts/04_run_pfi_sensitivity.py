"""Run Monte Carlo sensitivity checks for PFI component weighting."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from pfi_pipeline.config import OUTPUT_DIR, PROCESSED_DIR
from pfi_pipeline.io import read_table, require_columns, write_table


def main(iterations: int = 5000, seed: int = 42) -> None:
    input_path = PROCESSED_DIR / "pfi" / "pfi_merged.csv"
    df = read_table(input_path)
    require_columns(df, ["PCS_z", "TFS_z"], "pfi_merged.csv")

    rng = np.random.default_rng(seed)
    alpha = rng.uniform(0.50, 0.70, size=iterations)
    beta = 1.0 - alpha
    pcs = df["PCS_z"].to_numpy()
    tfs = df["TFS_z"].to_numpy()
    reference = (0.597 * pcs) + (0.403 * tfs)

    rows = []
    for idx, (a, b) in enumerate(zip(alpha, beta), start=1):
        candidate = (a * pcs) + (b * tfs)
        rows.append(
            {
                "iteration": idx,
                "alpha": a,
                "beta": b,
                "spearman_rho": pd.Series(reference).corr(
                    pd.Series(candidate), method="spearman"
                ),
                "pearson_r": pd.Series(reference).corr(pd.Series(candidate)),
            }
        )

    result = pd.DataFrame(rows)
    summary = result[["spearman_rho", "pearson_r"]].describe().reset_index()
    write_table(result, OUTPUT_DIR / "sensitivity_iterations.csv")
    write_table(summary, OUTPUT_DIR / "sensitivity_summary.csv")
    print(f"Sensitivity iterations written: {OUTPUT_DIR / 'sensitivity_iterations.csv'}")
    print(f"Median Spearman rho: {result['spearman_rho'].median():.3f}")


if __name__ == "__main__":
    main()

