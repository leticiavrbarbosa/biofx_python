#!/usr/bin/env python3
"""
Author : leticiavrbarbosa <leticiavrbarbosa@localhost>
Date   : 2024-04-04
Purpose: Print the reverse complement of DNA
"""

import argparse
from typing import NamedTuple, TextIO
import os

# https://biopython.org/docs/1.75/api/Bio.Seq.html
from Bio.Seq import Seq

class Args(NamedTuple):
    """ Command-line arguments """
    positional: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='DNA',
                        help='Input sequence or file')

    args = parser.parse_args()

    return Args(args.positional)

# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    pos_arg = args.positional
    
    if os.path.isfile(pos_arg):
        pos_arg = open(pos_arg).read().strip()
    # print(pos_arg)
    
    revc = ''
    # complement = {'A':'T', 'a':'t', 
    #               'T':'A', 't':'a',
    #               'C':'G', 'c':'g',
    #               'G':'C', 'g':'c'}
    # for base in reversed(pos_arg):
    #     if base in complement:
    #         revc += complement[base]
    #     else: revc += base
    
    # list comprehension solution 
    # revc = [complement.get(base, base) for base in pos_arg]
    # print(''.join(reversed([complement.get(base, base) for base in pos_arg])))
    
    # start = "tTaAcCgG"
    # end = "aAtTgGcC"
    # # this creates a dictionary of character ascii values 
    # translation_table = str.maketrans(start, end)
    # # print(translation_table)
    # revc = pos_arg.translate(translation_table)
    
    revc = Seq(pos_arg)
    
    print(revc.reverse_complement())        

    
    


# --------------------------------------------------
if __name__ == '__main__':
    main()

# notes 
# dna[::-1] -> outputs the reversed string, where dna is the string 
# reversed(dna) -> iterator 
    # this prints out the reversed string: ''.join(reversed(dna))
# list(reversed(dna)) -> creates a list of the chars in dna 