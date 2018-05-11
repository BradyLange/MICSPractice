#!/usr/bin/env python3
# input format check for Problem 3

from sys import stdin
import sys
import re

whitespace = "[ \t]+"
white = re.compile(whitespace + "\n")

# read in the first line which is the number of scaling factors
line = stdin.readline()
assert white.match(line)

assert len(stdin.readline()) == 0
sys.exit(42)
# Nothing to report


