#!/usr/bin/env python3
# input format check for Problem 8
# Sample input
# 4
#-8
#10
#-13
#-4
 

from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"
oneint = re.compile(integer + "\n")


# read in the first line which is the number of scaling factors
line = stdin.readline()
assert oneint.match(line)
n = int(line)
assert n > 0

# read each line and check if it is a legal scale factor
for i in range(n):
   line = stdin.readline()
   assert oneint.match(line)

assert len(stdin.readline()) == 0
sys.exit(42)
# Nothing to report


