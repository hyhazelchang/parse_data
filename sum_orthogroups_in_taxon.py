#!/usr/bin/python3

# sum_orthogroups_in_taxon.py

# Hsin-Ying Chang <hyhazelchang@gmail.com>
# v1 2023/06/09

# Usage: python3 /home/xinchang/pyscript_xin/sum_orthogroups_in_taxon.py --input=/scratch/xinchang/cyano11/cyano11.11/orthomcl/group/all.stat --taxon_num=23 --output=/scratch/xinchang/cyano11/cyano11.11/orthomcl/group/OGs_sum.out

import argparse
import os

def main():
    parser = argparse.ArgumentParser(
            description=("Summarize the OGs in taxon!"),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--input",
                        type=str,
                        default=None,
                        help="Input file. Please provide absolute path.")
    parser.add_argument("--taxon_num",
                        type=str,
                        default=None,
                        help="Total taxon number.")
    parser.add_argument("--output",
                        type=str,
                        default="./output",
                        help="Output files. Please provide absolute path.")

    # Defining variables from input
    args = parser.parse_args()
    input = args.input
    taxon_num = int(args.taxon_num)
    output = args.output
    output_dir = os.path.dirname(output)

    # Create a new directory for sequences output
    if not os.path.exists(output_dir):
        os.system("mkdir -p " + output_dir)

    # Parse out the lines
    lines = [line.rstrip("\n").split() for line in open(input)]

    # Add hashtags by taxon numbers
    orthogroups = {}
    for num in range(taxon_num):
        orthogroups.update({str(num + 1) : int(0)})

    # Calculate the number of OGs in each taxa
    for line in lines:
        taxa = line[1].split(":")[0]
        for key in orthogroups.keys():
            if key == taxa:
                orthogroups[key] += 1
    
    # Write to output
    out = open(output, "w")
    for key, value in orthogroups.items():
        out.write(key + "\t" + str(value) + "\n")
    out.close()

if __name__ == '__main__':
    main()