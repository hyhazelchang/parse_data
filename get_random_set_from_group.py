#!/usr/bin/python3

# get_random_set_from_group.py

# Hsin-Ying Chang <hyhazelchang@gmail.com>
# v1 2023/06/09

# Usage: python3 /home/xinchang/pyscript_xin/get_random_set_from_group.py --input=/scratch/xinchang/cyano11/cyano11.21/group/cyano11.11.group --output_dir=/scratch/xinchang/cyano11/cyano11.21/group --rep=3

import argparse
import os
from itertools import combinations
import random

def main():
    parser = argparse.ArgumentParser(
            description=("Get random sets from group list"),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--input",
                        type=str,
                        default=None,
                        help="Input file. Please provide absolute path.")
    parser.add_argument("--output_dir",
                        type=str,
                        default="./output",
                        help="Output directory. Please provide absolute path.")
    parser.add_argument("--rep",
                        type=int,
                        default=None,
                        help="How many group do you need? The number should not more than total genome number.")

    # Defining variables from input
    args = parser.parse_args()
    input = args.input
    output_dir = args.output_dir
    rep = args.rep

    # Create a new directory for sequences output
    if not os.path.exists(output_dir):
        os.system("mkdir -p " + output_dir)

    # Parse out the lines
    lines = [line.rstrip("\n").split() for line in open(input)]

    # Combinations of groups
    for i in range(2, len(lines)):
        groups = list(combinations(lines, i))
        sampling = random.sample(groups, rep)
        for m in range(len(sampling)):
            number = str(i) + "-" + str(m + 1)
            outfile = output_dir + "/" + number + ".group"
            out = open(outfile, "w")
            for n in range(i):
                out.write(sampling[m][n][0] + "." + number + "\t" + sampling[m][n][1] + "\n")
            out.close()

if __name__ == '__main__':
    main()
