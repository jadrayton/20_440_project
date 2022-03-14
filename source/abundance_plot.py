#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys, getopt
import os
from IPython.display import display

def main(argv):
    # Read inputs from command line
    inputfiles = []
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"i:o:")
    except getopt.GetoptError:
        print('abundance_plot.py -i <inputfiles> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-i":
            inputfiles.append(arg)
        elif opt == "-o":
            outputfile = arg
    sample_names = []
    # Generate sample names for plot legend
    for file in inputfiles:
        if file[:30] == 'salmon_harmonized_transcripts_':
            # Trim unnecessary standard info for cleaner legend
            sample = file[30:]
            sample = sample[:-4]
            sample_names.append(sample)
        else:
            sample_names.append(file[:-4])
    # Associate samples with corresponding files
    sample_dict = dict(zip(sample_names, inputfiles))
    abundance_df = pd.DataFrame(columns=sample_names)
    os.chdir('../processed') # Directory containing processed data files
    for sample in sample_names:
        data = np.loadtxt(sample_dict[sample], skiprows=1, usecols=-1) # Loading "Counts" column
        abundance_df.loc[:,sample]=data
    # Plot histogram
    ax = abundance_df.plot.hist(bins=10, logy=True, ylim=(1,5*10**5), alpha=0.5)
    ax.set_xlabel('Counts')
    os.chdir('../plots') # Directory to save plots
    plt.savefig(outputfile)
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])