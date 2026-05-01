# Zenodo Workflow

This repository is prepared for GitHub-to-Zenodo archival after manuscript acceptance or when journal policy permits public release.

## Recommended Steps

1. Finalize the public repository contents.
2. Remove any unpublished manuscript files, reviewer-only documents, API keys, raw imagery, and restricted third-party data.
3. Create a GitHub release, for example `v1.0.0`.
4. Connect the GitHub repository to Zenodo.
5. Archive the release on Zenodo and reserve or publish the DOI.
6. Add the Zenodo DOI badge to `README.md`.
7. Update the manuscript data availability statement if required by the journal.

## Suggested Release Assets

- Source code.
- Processed tabular data.
- Variable dictionary.
- Sampling metadata.
- Model outputs required to reproduce tables.
- Figure-generation scripts where copyright and journal policy allow.

## Materials to Exclude

- Raw Google Street View images.
- API keys and credentials.
- Local logs and cache files.
- Submitted manuscript PDFs during peer review.
- Any file containing private paths, personal notes, or unreleased journal material.

