""" Tests for dna.py """

import os
from subprocess import getstatusoutput, getoutput

PRG = './dna.py'
TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.exists(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage with no args or for help """

    for arg in ['', '-h', '--help']:
        out = getoutput(f'{PRG} {arg}')
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_arg():
    """ Uses command-line arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()
        retval, out = getstatusoutput(f'{PRG} {dna}')
        assert retval == 0
        assert out == expected


# --------------------------------------------------
def test_file():
    """ Uses file arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        retval, out = getstatusoutput(f'{PRG} {file}')
        assert retval == 0
        assert out == expected