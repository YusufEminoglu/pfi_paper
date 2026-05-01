"""Shared configuration for public reproducibility scripts."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT / "outputs" / "public"

RESPONSE_COLUMN = "PFI"

COMPONENT_COLUMNS = {
    "PCS_z": "Physical Comfort Score, standardized",
    "TFS_z": "Thermal Friction Score, standardized",
}

PFI_WEIGHTS = {
    "PCS_z": 0.597,
    "TFS_z": 0.403,
}

BASE_PREDICTORS = [
    "ECW_m",
    "MDI",
    "SCR",
    "FAR_node",
    "H_std",
    "BC",
    "JCS",
    "DPark",
    "SLOPE",
    "GAR",
    "TCH",
]

INTERACTIONS = {
    "ECW_m_x_BC": ("ECW_m", "BC"),
    "MDI_x_GAR": ("MDI", "GAR"),
    "BC_x_DPark": ("BC", "DPark"),
    "SLOPE_x_SCR": ("SLOPE", "SCR"),
}

IDENTIFIER_COLUMNS = [
    "node_id",
    "hex_id",
    "district",
    "lon",
    "lat",
]

