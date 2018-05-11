#!/usr/bin/env python3
# input format check for Problem 1
# Sample input
# 2
# 1
# 3
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
assert n <= 100

# read each line and check if it is a legal scale factor
for i in range(n):
   line = stdin.readline()
   assert oneint.match(line)
   size = int(line)
   assert size > 0
   assert size <= 50

assert len(stdin.readline()) == 0
sys.exit(42)
# Nothing to report


