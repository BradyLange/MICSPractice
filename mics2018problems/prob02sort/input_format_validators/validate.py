#!/usr/bin/env python3
# input format check for Problem 2
# Sample input
# 9
# 4.0 0.0 -3.0 0.0 -7.0 0.0 2.0 2.0 5.0 0.0 0.0 0.0 7.0 0.0 0.5 -1.3 6.5 0.9
from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"
oneint = re.compile(integer + "\n")
twoint = re.compile(integer + " " + integer + "\n")
manyint = re.compile("(" + integer + " )*" + integer + "\n")

decimal =  "[-+]?[0-9]*\.?[0-9]+"
onedec = re.compile(decimal + "\n")
twodec = re.compile(decimal + " " + decimal + "\n")
manydec = re.compile("(" + decimal + " )*" + decimal + "\n")

# read in the first line which is an integer
line = stdin.readline()
assert oneint.match(line)
n = int(line)
assert n > 0

# read seoncd line
line = stdin.readline()
assert manydec.match(line)

assert len(stdin.readline()) == 0
sys.exit(42)
# Nothing to report


