#!/usr/bin/env python

import pandas as pd
from glob import glob

# Load results from kd prediction
locs = 'results/kdvals/*.txt'
files = glob(locs)
dfs = [pd.read_csv(file, sep=': ', index_col=0, engine='python').set_axis([file], axis=1) for file in files]
alldf = pd.concat(dfs, axis=1, join='inner')

# Transpose
df = alldf.T

# Rename
df['filename'] = df.index.copy()
df['filename'] = df['filename'].str.replace(r'(?<=/)(ABC_|AC_|BC_)', '', regex=True)
df['filename'] = df['filename'].str.replace('txt', 'pdb')
df['filename'] = df['filename'].str.replace('results/kdvals/', 'results/complexes/')

# Format the index columns
df.index = df.index.str.replace('.*\/','', regex=True)
names = df.index.str.split('_', expand=True).to_frame().reset_index()
df = df.reset_index(drop=True).iloc[:, 1:]
df.loc[:, 'Molecule_combination'] = names.iloc[:,0]
df.loc[:, 'Receptor'] = names.iloc[:,2]
df.loc[:, 'Hormone'] = names.iloc[:,3]
df = df.set_index(['Molecule_combination', 'Receptor', 'Hormone'])

# Save
df.to_csv('results/allkd.tsv', sep='\t')
