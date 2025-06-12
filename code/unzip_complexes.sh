#!/bin/bash

mkdir -p results/extracted results/complexes

for zipfile in data/*.zip; do
    base_name=$(basename $zipfile .result.zip)
    echo "Extracting $zipfile into results/${base_name}"
    unzip -q -d "results/extracted/${base_name}" "$zipfile"
done

mv results/extracted/*/*/*.pdb results/complexes/

rm -r results/extracted
