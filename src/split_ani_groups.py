#!/bin/env python

import sys
import pandas as pd

## Usage: python split_ani_groups.py <ANI_file.tsv> <ANI_threshold_1> <ANI_threshold_2>....<ANI_threshold_n>

## Parse ANI file
ani = pd.read_csv(sys.argv[1], delimiter="\t")
focal_strain = str(ani.iloc[0]['Reference']).rstrip('.0') ## rstrip for integer strain names
ani = ani[['Query', 'ANI']]

## Don't forget about the focal strain
fs = pd.DataFrame({ focal_strain: [100] }, columns=['Query', 'ANI'])
ani.append(fs)

## Assign groups based on commandline args
for threshold in sys.argv[2:]:
    threshold = float(threshold)
    in_t = ani['ANI'] > threshold
    ani['in_'+str(threshold)] = in_t

## Dump groups to file
ani.to_csv('in_groups.tsv', sep="\t")
