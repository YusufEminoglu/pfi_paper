"""Run transparent OLS baseline diagnostics for the public model matrix."""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from pfi_pipeline.config import BASE_PREDICTORS, INTERACTIONS, OUTPUT_DIR, RESPONSE_COLUMN
from pfi_pipeline.diagnostics import descriptive_summary, variance_inflation_table
from pfi_pipeline.io import read_table, write_table
from pfi_pipeline.modelling import cross_validated_ols, fit_ols


def main() -> None:
    model_path = OUTPUT_DIR / "model_matrix.csv"
    df = read_table(model_path)
    predictors = [*BASE_PREDICTORS, *INTERACTIONS.keys()]

    fitted = fit_ols(df, RESPONSE_COLUMN, predictors)
    cv = cross_validated_ols(df, RESPONSE_COLUMN, predictors, group_column="hex_id")
    vif = variance_inflation_table(df, predictors)
    summary = descriptive_summary(df, [RESPONSE_COLUMN, *predictors])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_table(cv, OUTPUT_DIR / "baseline_cv_metrics.csv")
    write_table(vif, OUTPUT_DIR / "vif_table.csv")
    write_table(summary, OUTPUT_DIR / "descriptive_summary.csv")

    with (OUTPUT_DIR / "ols_summary.txt").open("w", encoding="utf-8") as file:
        file.write(fitted.summary().as_text())

    print(f"OLS summary written: {OUTPUT_DIR / 'ols_summary.txt'}")
    print(f"Cross-validation metrics written: {OUTPUT_DIR / 'baseline_cv_metrics.csv'}")
    print(f"Mean CV R2: {cv['r2'].mean():.3f}")


if __name__ == "__main__":
    main()

