#!/usr/bin/env python3
# input format check for Problem 6
# Sample input
#3 
#3 27 13 15 6 7 5 9 
#4 21 9 10 4 5 4 6 2 2 1 4 1 3 2 4 
#3 29 13 16 5 8 9 1

from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"
intsandspaces = "((0|-?[1-9]\d*).)*(0|-?[1-9]\d*)"
oneint = re.compile(integer + "\n")
manyint = re.compile(intsandspaces + "\n")

# read in the first line which is the number of scaling factors
line = stdin.readline()
assert oneint.match(line)
n = int(line)
assert n > 0

# read each line and check if it is a legal scale factor
for i in range(n):
   line = stdin.readline()
   assert manyint.match(line)

assert len(stdin.readline()) == 0
sys.exit(42)
# Nothing to report


