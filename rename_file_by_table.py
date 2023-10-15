#!/usr/bin/python3

# rename_file_by_table.py

# Hsin-Ying Chang <hyhazelchang@gmail.com>
# v1 2023/09/22

# Usage: python3 /home/xinchang/pyscript_xin/rename_file_by_table.py --in_dir=/scratch/xinchang/cyano11/cyano11.24/source_data/gb/ --out_dir=/scratch/xinchang/cyano11/cyano11.24/source_data/renamed_gb/ --table=/scratch/xinchang/cyano11/cyano11.24/list/download.list --in_file_ext="gbff" --out_file_ext="gb" --index_in=3 --index_out=0

import argparse
import os
import glob

def main():
    parser = argparse.ArgumentParser(
            description=("Parse the sequences from gb"),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--in_dir",
                        type=str,
                        default=None,
                        help="The directory of input files.")
    parser.add_argument("--out_dir",
                        type=str,
                        default=None,
                        help="The directory of output file.")
    parser.add_argument("--table",
                        type=str,
                        default=None,
                        help="The table for renaming.")
    parser.add_argument("--in_file_ext",
                        type=str,
                        default=None,
                        help="input file extension.")
    parser.add_argument("--out_file_ext",
                        type=str,
                        default=None)
    parser.add_argument("--index_in",
                        type=int,
                        default=None)
    parser.add_argument("--index_out",
                        type=int,
                        default=None)

    # Defining variables from input
    args = parser.parse_args()
    in_dir = args.in_dir
    out_dir = args.out_dir
    table = args.table
    in_file_ext = args.in_file_ext
    out_file_ext = args.out_file_ext
    index_in = args.index_in
    index_out = args.index_out

    # Create a new directory for sequences output
    if not os.path.exists(out_dir):
        os.system("mkdir -p " + out_dir)
    
    # Find table for renaming
    tb_file = [line.rstrip("\n").split("\t") for line in open(table)]

    # Get the genbank files in the input directory
    input = glob.glob(os.path.join(in_dir, "*." + in_file_ext))

    # Count the file number
    count_in = 0
    count_out = 0
    # Find the files from table
    for line in tb_file:
        count_in += 1
        file = in_dir + str(line[index_in]) + "." + in_file_ext
        if file in input:
            count_out += 1
            os.system("cp " + file + " " + out_dir + line[index_out] + "." + out_file_ext)
        else:
            print("There is no file: " + str(line[index_in]) + "." + in_file_ext + "! Failed to rename it")

if __name__ == '__main__':
    main()