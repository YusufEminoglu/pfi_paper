# Pedestrian Friction Mapping in Izmir

[![Status](https://img.shields.io/badge/status-pre--publication-0b6b6b)](#repository-status)
[![Journal target](https://img.shields.io/badge/target-Computers%2C%20Environment%20and%20Urban%20Systems-1f4e79)](#paper)
[![Code license](https://img.shields.io/badge/license-MIT-2f6f4e)](LICENSE)
[![Data availability](https://img.shields.io/badge/data-upon%20publication-7a5195)](docs/data_availability.md)

This repository is the public companion package for the manuscript:

**Dual Friction Mapping of Urban Pedestrian Spaces: Integrating Street-View Visual Analytics and Geographically Neural Network Weighted Regression in Izmir, Türkiye**

The study models sidewalk-level pedestrian friction across Google Street View nodes in the functional urban area of Izmir. It combines street-view semantic segmentation, Google Earth Engine thermal indicators, OpenStreetMap and Urbanity network metrics, built-form variables, stratified hexagonal sampling, spatial regression baselines, and geographically neural network weighted regression.

## Repository Status

This is a **pre-publication repository shell**. It is intentionally conservative:

- Raw Google Street View imagery is not redistributed.
- API keys, tokens, local configuration files, logs, cache files, and virtual environments are excluded.
- Manuscript source files, submitted PDFs, journal figures, and full-resolution production outputs are not included during peer review.
- Reproducible code, processed tabular data, derived image metrics, and metadata will be released and archived through Zenodo after publication or when journal policy permits.

## Paper

The manuscript examines pedestrian friction as an urban-environment response variable:

```text
PFI = f(pedestrian-space capacity,
        urban morphology,
        network exposure,
        terrain effort,
        green-infrastructure buffering,
        local spatial interactions)
```

The empirical workflow is based on 126 sampled hexagons and 6,771 Google Street View nodes. The response variable is the Pedestrian Friction Index (PFI), while explanatory variables represent visual walking capacity, morphology, network structure, park access, slope, and green infrastructure.

## Repository Layout

```text
pfi_paper/
├── README.md
├── LICENSE
├── CITATION.cff
├── .zenodo.json
├── .gitignore
├── requirements.txt
├── data/
│   └── README.md
├── docs/
│   ├── data_availability.md
│   ├── reproducibility.md
│   └── zenodo_workflow.md
├── figures/
│   └── README.md
├── metadata/
│   └── variable_dictionary.csv
├── src/
│   └── README.md
└── workflow/
    └── pipeline_manifest.yml
```

## Authors

| Author | Affiliation | Profiles |
|---|---|---|
| **Yusuf Eminoğlu** | Department of City and Regional Planning, Dokuz Eylül University; LUQAA - Lab of Urban Analytics and Quantitative Analysis | [![GitHub](https://img.shields.io/badge/GitHub-YusufEminoglu-181717?logo=github)](https://github.com/YusufEminoglu) [![ORCID](https://img.shields.io/badge/ORCID-0009--0005--6000--2934-a6ce39?logo=orcid)](https://orcid.org/0009-0005-6000-2934) [![ResearchGate](https://img.shields.io/badge/ResearchGate-profile-00ccbb?logo=researchgate)](https://www.researchgate.net/profile/Yusuf-Eminoglu?ev=hdr_xprf) [![AVESIS](https://img.shields.io/badge/AVESIS-DEU-004b8d)](https://avesis.deu.edu.tr/yusuf.eminoglu) |
| **Kemal Mert Çubukçu** | Department of City and Regional Planning, Dokuz Eylül University; Founder, LUQAA - Lab of Urban Analytics and Quantitative Analysis | [![ORCID](https://img.shields.io/badge/ORCID-0000--0003--3604--7014-a6ce39?logo=orcid)](https://orcid.org/0000-0003-3604-7014) [![ResearchGate](https://img.shields.io/badge/ResearchGate-profile-00ccbb?logo=researchgate)](https://www.researchgate.net/profile/K-Mert-Cubukcu) [![AVESIS](https://img.shields.io/badge/AVESIS-DEU-004b8d)](https://avesis.deu.edu.tr/mert.cubukcu) |

## Data Availability

Processed data, code, and reproducible analysis scripts will be deposited in this GitHub repository and archived through Zenodo upon publication. Raw Google Street View imagery is subject to third-party licensing restrictions and will not be redistributed publicly; derived metrics and image metadata will be provided, and additional research materials may be made available from the corresponding author upon reasonable request.

## License

Code released in this repository is licensed under the MIT License. Data and figure assets may be released under a separate license after publication, depending on journal policy, third-party data restrictions, and Zenodo deposition requirements.

