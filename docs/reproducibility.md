# Reproducibility Notes

This repository is designed to support transparent reproduction of the manuscript after publication while respecting third-party data restrictions.

## Computational Workflow

The study workflow has six main stages:

1. Construct the spatial sampling frame using H3 hexagons.
2. Apply eligibility filters and stratified morphological sampling.
3. Generate Google Street View nodes on the pedestrian network.
4. Extract visual, thermal, network, morphology, terrain, park-access, and canopy metrics.
5. Construct the node-level Pedestrian Friction Index response variable.
6. Estimate and compare OLS, spatial lag, GWR, MGWR, and GNNWR models.

## Coordinate Reference Systems

- Storage and visualization: EPSG:4326.
- Distance and area calculations: EPSG:32635.

## Reproduction Boundary

The exact raw Google Street View imagery cannot be redistributed. The planned reproducibility package will therefore reproduce the analytical pipeline from processed image-derived metrics and metadata, not from raw image files.

## Environment

The project uses a Python geospatial stack with `geopandas`, `osmnx`, `rasterio`, `earthengine-api`, `libpysal`, `spreg`, `mgwr`, `scikit-learn`, and related packages. The final locked environment file will be added with the publication release.

