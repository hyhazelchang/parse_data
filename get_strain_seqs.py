#!/usr/bin/python3

# get_strain_seqs.py

# Hsin-Ying Chang <hyhazelchang@gmail.com>
# v1 2023/05/29

# Usage: python3 /home/xinchang/pyscript_xin/get_strain_seqs.py --in_dir=/scratch/xinchang/cyano11/cyano11.20/ortho_fasta/all+1 --out_dir=/scratch/xinchang/cyano11/cyano11.20/aa_fasta --ext=fasta --prefix=JW907

import argparse
import os, glob

def main():
    parser = argparse.ArgumentParser(
            description=("Get strain sequences from ortho fasta."),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--in_dir",
                        type=str,
                        default=None,
                        help="Input directory. Please provide the abosolute pathway.")
    parser.add_argument("--ext",
                        type=str,
                        default="fasta",
                        help="Please provide the extensions of sequence files.")
    parser.add_argument("--prefix",
                        type=str,
                        default=None,
                        help="Prefix of strain sequences")
    parser.add_argument("--out_dir",
                        type=str,
                        default=None,
                        help="Output directory. Please provide the abosolute pathway.")

    # Defining variables from inputs
    args = parser.parse_args()
    in_dir = args.in_dir
    prefix = args.prefix
    out_dir = args.out_dir

    inputs = glob.glob(os.path.join(in_dir, "*.%s" % args.ext))

    # Make out_dir directory
    if not os.path.exists(out_dir):
        os.system("mkdir -p " + out_dir)

    # open the sequences files
    id_seqs = []
    for file in inputs:
        filename = os.path.basename(file).split(".")[0]
        lines = [line.rstrip("\n") for line in open(file)]
        i = 0
        while i < len(lines):
            if prefix in lines[i]:
                id_seqs.append(lines[i] + "_" + filename)
                id_seqs.append(lines[i+1])
            i += 2

    # write into the out_dir
    out_dir = open(out_dir + "/" + prefix + ".fasta", "w")
    for id_seq in id_seqs:
        out_dir.write(id_seq + "\n")
    out_dir.close()

if __name__ == "__main__":
    main()