#!/bin/bash

mkdir -p results/kdvals

# Iterate over all .pdb files in the directory
for file in $1
do
    # Get the base name of the file without the extension
    name=$(basename "$file" .pdb)
    
    # Display the base name
    echo "Processing file: $name"
    
    # Run prodigy with selection A and C, and save the output
    prodigy "$file" --selection A C > "results/kdvals/AC_${name}.txt"
    prodigy "$file" --selection B C > "results/kdvals/BC_${name}.txt"
    prodigy "$file" --selection A,B C > "results/kdvals/ABC_${name}.txt"
done
