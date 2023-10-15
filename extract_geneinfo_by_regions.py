#!/usr/bin/python3

# extract_geneinfo_by_regions.py

# Hsin-Ying Chang <hyhazelchang@gmail.com>
# v1 2023/10/11

# Usage: python3 /home/xinchang/pyscript/pyscript_xin/extract_geneinfo_by_regions.py --info=/scratch/xinchang/cyano11/cyano11.28/run_1_18.info --listfile=/scratch/xinchang/cyano11/cyano11.28/cg_sweep/output/cyano11_28.0.0.core_sweeps.csv --output=/scratch/xinchang/cyano11/cyano11.28/genes_sweep --index_from=1 --index_to=2


import argparse
import os
import pandas as pd

def main():
    parser = argparse.ArgumentParser(
        description=("Extract info of genes by a list."),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--info",
                        default=None,
                        type=str,
                        help="Gene info list. Please provide absolute path.")
    parser.add_argument("--listfile",
                        default=None,
                        type=str,
                        help="Region list for extract info")
    parser.add_argument("--output",
                        default=None,
                        type=str,
                        help="Output file. Please provide absolute path.")
    parser.add_argument("--index_from",
                        default=None,
                        type=int)
    parser.add_argument("--index_to",
                        default=None,
                        type=int)

    args = parser.parse_args()
    info = args.info
    listfile = args.listfile
    output = args.output
    index_from = args.index_from
    index_to = args.index_to
    out_dir = os.path.dirname(output)

    # Make output directory
    if not os.path.exists(out_dir):
        os.system("mkdir -p " + out_dir)

    # Parse info and list
    info_lines = [line.rstrip("\n").split("\t") for line in open(info)]
    region_list = pd.read_table(listfile, delimiter=",")

    # Extract and write into output
    regions = []
    for i, row in region_list.iterrows():
        regions.append((row[index_from], row[index_to]))
    
    extract = []
    for region in regions:
        for line in info_lines:
            if int(line[3]) >= int(region[0]) and int(line[4]) <= int(region[1]):
                extract.append(line)

    out = open(output, "w")
    for line in extract:
        out.write("\t".join(line) + "\n")
    out.close()

if __name__ == "__main__":
    main()