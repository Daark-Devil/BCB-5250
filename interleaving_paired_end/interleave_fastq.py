#!/usr/bin/env python3


from Bio import SeqIO
import sys

def interleave_fastq(forward_file, reverse_file, output_file):
    with open(output_file, "w") as out_f:
      
        forward_reads = SeqIO.parse(forward_file, "fastq")
        reverse_reads = SeqIO.parse(reverse_file, "fastq")

        for f_read, r_read in zip(forward_reads, reverse_reads):
          
            SeqIO.write(f_read, out_f, "fastq")
            SeqIO.write(r_read, out_f, "fastq")

    print(f"Interleaving completed and Output saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python interleave_fastq.py 1)forward_reads.fastq> 2)<reverse_reads.fastq> 3) <output.fastq>")
        sys.exit(1) 

   
    forward_file = sys.argv[1]
    reverse_file = sys.argv[2]
    output_file = sys.argv[3]

    
    interleave_fastq(forward_file, reverse_file, output_file)
