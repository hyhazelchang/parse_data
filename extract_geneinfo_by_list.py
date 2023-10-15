#!/usr/bin/python3

# extract_geneinfo_by_list.py

# Hsin-Ying Chang <hyhazelchang@gmail.com>
# v1 2023/06/04
# v2 2023/09/13 add index input

# Usage: python3 /home/xinchang/pyscript_xin/extract_geneinfo_by_list.py --info=/scratch/xinchang/cyano17/cyano17.03/source_data/info/cyano17.03.info --listfile=/scratch/xinchang/cyano17/cyano17.03/farlip.list --output=/scratch/xinchang/cyano17/cyano17.03/source_data/cds/info/farlip_info.txt --index_in=2 --index_info=2


import argparse
import os

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
                        help="Gene list for extract info")
    parser.add_argument("--output",
                        default=None,
                        type=str,
                        help="Output file. Please provide absolute path.")
    parser.add_argument("--index_in",
                        default=None,
                        type=int)
    parser.add_argument("--index_info",
                        default=None,
                        type=int)

    args = parser.parse_args()
    info = args.info
    listfile = args.listfile
    output = args.output
    index_in = args.index_in
    index_info = args.index_info
    out_dir = os.path.dirname(output)

    # Make output directory
    if not os.path.exists(out_dir):
        os.system("mkdir -p " + out_dir)

    # Parse info and list
    info_lines = [line.rstrip("\n").split("\t") for line in open(info)]
    gene_list = [gene.rstrip("\n").split("\t") for gene in open(listfile)]

    # Extract and write into output
    extract_list = []
    for gene in gene_list:
        for line in info_lines:
            if gene[index_in] == line[index_info]:
                extract_list.append(line[0])
    
    extract = []
    for num in extract_list:
        for line in info_lines:
            if num == line[0]:
                extract.append(line)

    out = open(output, "w")
    for line in extract:
        out.write("\t".join(line) + "\n")
    out.close()

if __name__ == "__main__":
    main()