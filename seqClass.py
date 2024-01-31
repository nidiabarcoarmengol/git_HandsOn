#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Create an ArgumentParser object with descriptions for command-line arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')

# Define command-line arguments
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Check if no command-line arguments are provided, print help, and exit if true
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the command-line arguments
args = parser.parse_args()

# Convert the sequence to uppercase
args.seq = args.seq.upper()                 # Note we just added this line

# Check if the sequence consists of valid DNA or RNA characters
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# If a motif is provided, convert it to uppercase and search for it in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("The motif was FOUND")
    else:
        print("NOT FOUND")

