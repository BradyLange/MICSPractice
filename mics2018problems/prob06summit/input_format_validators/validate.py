#!/usr/bin/env python3
# input format check for Problem 6
# Sample input
#2 
#8 7 3 2 3 5 4 0 1 4 5 3 2 2 2 
#3 3 1 0 0 3 3

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


