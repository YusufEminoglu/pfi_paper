# Source Code

This directory contains the reusable Python utilities used by the public reproducibility scripts.

The public source code focuses on the parts of the workflow that can be shared safely before the full data release:

- model-matrix construction,
- PFI calculation,
- interaction-term generation,
- descriptive diagnostics,
- VIF diagnostics,
- transparent OLS baseline evaluation,
- Monte Carlo sensitivity checks.

The full private research pipeline also includes data acquisition, Google Street View downloading, Google Earth Engine extraction, semantic segmentation, raw figure production, and journal production scripts. Those components require additional cleaning before release because they interact with credentials, third-party imagery, large local files, and manuscript-production material.
