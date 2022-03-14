# Overview

This repository contains preprocessed data and code to generate plots for the 20.440 project "Investigation of AIRE Gene Transcription and Epitopes in Autoimmunity," as well as the generated plots.

# Data

Data were sourced from Sansom et. al. and can be accessed through [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1470483).

    Sansom SN, Shikama-Dorn N, Zhanybekova S, Nusspaumer G et al. Population and single-cell genomics reveal the Aire dependency, relief from Polycomb silencing, and distribution of self-antigen expression in thymic epithelia. Genome Res 2014 Dec;24(12):1918-31. PMID: 25224068

The sample plot was generated using data from these accession numbers:
- [GSM1470483/SRX674408](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1470483)
- [GSM1470502/SRX674427](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1470502)

Fastq files can be downloaded from [NCBI Sequence Read Archive](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=search_seq_name).

## Data Preprocessing

*Note: Due to the size of the data files and Git LFS space limitations, these steps must be performed locally.*

Raw Fastq files were downloaded and unzipped, and blank lines at the end of the files were manually removed. Trimmed files were analyzed using [RNA Detector](https://github.com/alessandrolaferlita/RNAdetector).

    La Ferlita A, Alaimo S, Di Bella S, Martorana E, Laliotis GI, Bertoni F, Cascione L, Tsichlis PN, Ferro A, Bosotti R, Pulvirenti A. RNAdetector: a free user-friendly stand-alone and cloud-based system for RNA-Seq data analysis. BMC Bioinformatics. 2021 Jun 3;22(1):298. doi: 10.1186/s12859-021-04211-7.

 RNA Detector requires [Docker](https://www.docker.com/products/docker-desktop). .txt files output from RNA Detector can be found in the ./processed directory. 

## Data Processing

To generate plots, navigate to the ./source directory and run abundance_plot.py. You can designate any number of input files (-i \<filename\>) and an output file to store the plot (-o \<filename\>); you must designate at least one input file and exactly one output file. This script generates a histogram of sequence counts in each input sample and plots them all on the same axes. The completed plot will be stored in the ./plots directory.

# Folder Structure

./plots: Stores plots of processed data.

./processed: Stores preprocessed data for plotting

./source: Stores scripts for plotting (and potentially other functions in the future).

# Installation

The following packages and software are required to perform all the actions in the pipeline. Version numbers that were used to create the contents of this repo are in parentheses. 

- Python (3.8.8)
- NumPy (1.20.1)
- Pandas (1.2.4)
- MatPlotLib (3.3.4)
- IPython (7.22.0)
- RNA Detector (0.0.4)
- Docker Desktop (20.10.12)