#!/usr/bin/env python3

# Import necessary module from BioPython
from Bio import SeqIO
import sys

def interleave_fastq(forward_file, reverse_file, output_file):
    """
    This function interleaves reads from two paired-end FASTQ files (forward and reverse)
    and writes them to a single output FASTQ file.
    """
    try:
        # Open the output FASTQ file for writing
        with open(output_file, "w") as out_f:
            # Use BioPython's SeqIO to read both FASTQ files simultaneously
            forward_reads = SeqIO.parse(forward_file, "fastq")
            reverse_reads = SeqIO.parse(reverse_file, "fastq")

            # Loop through both files at the same time
            for f_read, r_read in zip(forward_reads, reverse_reads):
                # Write forward read to the output file
                SeqIO.write(f_read, out_f, "fastq")
                # Write reverse read to the output file
                SeqIO.write(r_read, out_f, "fastq")

        print(f"✅ Interleaving completed! Output saved to {output_file}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")


# Main function: Run the script from the command line
if __name__ == "__main__":
    # Check if the user provided the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python interleave_fastq.py <forward_reads.fastq> <reverse_reads.fastq> <output.fastq>")
        sys.exit(1)  # Exit if arguments are incorrect

    # Assign input/output filenames from command-line arguments
    forward_file = sys.argv[1]
    reverse_file = sys.argv[2]
    output_file = sys.argv[3]

    # Call the function to interleave reads
    interleave_fastq(forward_file, reverse_file, output_file)

