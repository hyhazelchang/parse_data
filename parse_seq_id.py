#!/usr/bin/python3

# parse_seq_id.py

# Hsin-Ying Chang <dnx202138@gmail.com>
# v1 2022/11/22

# Usage: python3 /home/xinchang/pyscript/parse_seq_id.py --input=/home/xinchang/seqs/16S_27F_1492R/Thermoleptolyngbya_XL5.fasta > /scratch/xinchang/cyano11/cyano11.04/list/16S.txt

import argparse
from Bio import SeqIO

def main():
    parser = argparse.ArgumentParser(
            description=("Parse the sequence id from fasta"),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--input",
                        type=str,
                        default=None,
                        help="input file.")

    # Defining variables from input
    args = parser.parse_args()
    in_file = args.input

    with open(in_file, "r") as seqfile:
        for record in SeqIO.parse(seqfile, "fasta"):
            print ("%s" % record.id)

if __name__ == '__main__':
    main()