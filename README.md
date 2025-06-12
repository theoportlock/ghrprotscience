# Binding Affinity Prediction for GHA2 and GHA3 Complexes

This repository accompanies the manuscript:

**"Growth hormone receptor antagonists, GHA2 and GHA3, with dual activity against the human and mouse receptor"**

It contains scripts used to extract, process, and analyze binding affinity predictions for Alphafold2-generated complexes involving human (HGHR) and mouse (MGHR) growth hormone receptors.
Data for the complexes are avaiable upon request.

---

## Overview

The analysis pipeline performs the following steps:

1. **Extracts PDB complexes** from compressed Alphafold2 output files.
2. **Renames PDB files** to standardize naming conventions for downstream processing.
3. **Predicts binding affinities (kD)** using [PRODIGY](https://wenmr.science.uu.nl/prodigy/).
4. **Aggregates** and merges all kD results into a summary table (`allkd.tsv`).

---

## Directory Structure

```
.
├── commands.sh             # Main script to run the full analysis pipeline
├── code/
│   ├── unzip_complexes.sh  # Extracts .pdb files from .zip archives
│   ├── rename_complexes.py # Standardizes naming of complex files
│   ├── kdpredict.sh        # Runs PRODIGY predictions on all complexes
│   └── mergekd.py          # Merges all PRODIGY outputs into a final table
└── results/                # Folder for results
```

---

## Usage

From the root directory, run:

```bash
bash commands.sh
```

Ensure the following before running:
- Alphafold2 `.zip` outputs are placed in the `data/` directory.
- PRODIGY is installed and available on your `$PATH`.

---

## Dependencies

- Python ≥ 3.6
- `pandas`
- Python packages in requirements.txt
- `bash` and `unzip`

---

## Output

The main output of this pipeline is:

```
results/allkd.tsv
```

A tab-separated summary table with predicted binding affinities (`kD`) for:
- Each PDB complex
- Multiple chain selections (`AC`, `BC`, `ABC`)
- Parsed molecule/receptor/hormone identities

---

## Contact

Theo Portlock  
Liggins Institute, University of Auckland  
