#!/usr/bin/env python3

import sys

# Initialize a variable to store headers for samples
samples_header = None

# Read from standard input line by line
for line in sys.stdin:
    if line.startswith('##'):
        continue  # Ignore meta-information lines
    elif line.startswith('#'):
        # This is the header line with sample names
        fields = line.strip().split('\t')
        samples_header = fields[9:]  # The sample names start from the 10th column
        print("CHROM\tPOS\tREF\tALT\tQUAL\tFILTER\t" + "\t".join(samples_header))
    else:
        fields = line.strip().split('\t')
        chrom = fields[0]
        pos = fields[1]
        ref = fields[3]
        alt = fields[4]
        qual = fields[5]  # Quality value
        filter_val = fields[6]  # Filter value
        format_info = fields[8].split(':')

        # Identify the position of the GT (Genotype) field
        gt_idx = format_info.index('GT')

        # Extract genotype information for each sample
        genotypes = []
        for sample_data in fields[9:]:
            sample_info = sample_data.split(':')
            gt = sample_info[gt_idx]
            genotypes.append(gt)

        # Print data in table format
        print(f'{chrom}\t{pos}\t{ref}\t{alt}\t{qual}\t{filter_val}\t' + "\t".join(genotypes))
