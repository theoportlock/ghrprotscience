#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Directory containing the PDB files you want to rename
source_folder = 'results/complexes/'

# Iterate over all files in the folder
for fname in os.listdir(source_folder):
    # Only process .pdb files
    if not fname.endswith('.pdb'):
        continue

    # Check if the file name already starts with 'MGHR' or 'HGHR'
    if fname.startswith('MGHR') or fname.startswith('HGHR'):
        print(f"Skipping '{fname}' (already renamed).")
        continue

    # Construct the new file name by prepending "MGHR_MGHR_"
    new_fname = "MGHR_MGHR_" + fname

    # Build full file paths for renaming
    old_path = os.path.join(source_folder, fname)
    new_path = os.path.join(source_folder, new_fname)

    # Rename the file
    print(f"Renaming '{old_path}' to '{new_path}'")
    os.rename(old_path, new_path)

