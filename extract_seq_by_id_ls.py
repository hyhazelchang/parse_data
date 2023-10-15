#!/usr/bin/python3

# extract_seq_by_id_ls.py

# Hsin-Ying Chang <hyhazelchang@gmail.com>
# v1 2023/06/09
# v2 2023/10/14 add funtions to parse out the seqs by groups

# Please check your data before using!!
## Usage (w/o grouping): python3 /home/xinchang/pyscript_xin/extract_seq_by_id_ls.py --input=/scratch/xinchang/cyano10/cyano10.18/blast_16S/16S.fasta --list=/scratch/xinchang/cyano10/cyano10.18/blast_16S/16S_download.list --output_dir=/scratch/xinchang/cyano10/cyano10.18/fasta --base_name=16S_extract2.fasta --index_in=1 --index_out=1
## Usage (w/ grouping): python3 /home/xinchang/pyscript_xin/extract_seq_by_id_ls.py --input=/scratch/xinchang/cyano11/cyano11.24/source_data/nt_fasta/cyano11.24.fasta --list=/scratch/xinchang/cyano11/cyano11.29/source_data/info/TA1pop_all+1_sweeps.txt --output_dir=/scratch/xinchang/cyano11/cyano11.29/source_data/nt_fasta/ --index_in=2 --index_out=1 --groups=1


import argparse
from Bio import SeqIO
import os

def main():
    parser = argparse.ArgumentParser(
            description=("Parse the sequences from fasta by id list"),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--input",
                        type=str,
                        default=None,
                        help="input file.")
    parser.add_argument("--list",
                        type=str,
                        default=None,
                        help="list file.")
    parser.add_argument("--output_dir",
                        type=str,
                        default="./output",
                        help="Directory for output files. Please provide absolute path.")
    parser.add_argument("--basename",
                        type=str,
                        default="seqout.fasta",
                        help="Base name for output file.")        
    parser.add_argument("--index_in",
                        type=int,
                        default=0,
                        help="id columns.")
    parser.add_argument("--index_out",
                        type=int,
                        default=0,
                        help="out columns.")
    parser.add_argument("--groups",
                        type=int,
                        default=0,
                        help="If you want to seperate the files into group or not.")

    # Defining variables from input
    args = parser.parse_args()
    input_file = args.input
    list_file = args.list
    output_dir = args.output_dir
    in_col = args.index_in
    out_col = args.index_out
    sep_groups = args.groups

    # Create a new directory for sequences output
    if not os.path.exists(output_dir):
        os.system("mkdir -p " + output_dir)

    # Concact the name columns and run name columns
    if sep_groups:
        sep_ids = sep_ids_ls(list_file, in_col, out_col)
    else:
        ids = ids_ls(list_file, in_col, out_col)    

    # Count the sequence number
    count_in = 0
    count_out = 0
    # Extract the ids and sequences out to the new file
    for record in SeqIO.parse(input_file, "fasta"):
        count_in += 1
        if sep_groups:
            for group in sep_ids.keys():
                for id in sep_ids[group]:
                    if id[0] in record.description:
                        id[0] = record.id   
                    if id[0] == record.id: 
                        count_out += 1
                        seq_id = id[1]
                        id[1] = ">" + seq_id + "\n" + str(record.seq) + "\n"
        else:
            for id in ids:
                if id[0] in record.description:
                    id[0] = record.id   
                if id[0] == record.id: 
                    count_out += 1
                    seq_id = id[1]
                    id[1] = ">" + seq_id + "\n" + str(record.seq) + "\n"
    
    # Write to output file
    if sep_groups:
        for group in sep_ids.keys():
            output = open(output_dir + str(group) + ".fasta", "w")
            for id in sep_ids[group]:
                output.write(id[1])
            output.close()
    else:
        basename = args.basename
        output = open(output_dir + basename + ".fasta", "w")
        for id in ids:
            output.write(id[1])
        output.close()
    
    # Show the counts
    print("count_in = " + str(count_in) + "\n" + "count_out = " + str(count_out) + "\n")

def ids_ls(list_file, in_col, out_col):
    ids = []
    with open(list_file) as ls:  
        for line in ls:
            cols = line.rstrip("\n").split("\t")
            ids.append([cols[in_col], cols[out_col]])
    return ids

def sep_ids_ls(list_file, in_col, out_col):
    sep_ids = {}
    with open(list_file) as ls:
        for line in ls:
            cols = line.rstrip("\n").split("\t")
            if str(cols[0]) in sep_ids.keys():
                sep_ids[str(cols[0])].append([cols[in_col], cols[out_col]])
            else:
                sep_ids[str(cols[0])] = [[cols[in_col], cols[out_col]]]
    return sep_ids

if __name__ == '__main__':
    main()
