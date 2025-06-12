#!/bin/bash
# Scripts for the processing and analysis of binding affinity of Alphafold2 complexes
# Author: Theo Portlock

# Export the code to run from root
export PATH=$PATH:code/

# Extract the complexes from the Alphafold compressed output
unzip_complexes.sh

# Rename the complex filenames
rename_complexes.py

# Predict kD and binding site characteristics between molecules for all complexes
kdpredict.sh 'results/complexes/*.pdb'

# Merge the affinities into one table
mergekd.py

