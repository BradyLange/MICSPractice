#!/usr/bin/env python3
# input format check for Problem 4
# Sample input
# 1 500000

from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"
decimal =  "[-+]?[0-9]*\.?[0-9]+"
oneint = re.compile(integer + "\n")
twoint = re.compile(integer + " " + integer + "\n")

# read in the first line which is two integers
line = stdin.readline()
assert twoint.match(line)
t, n = list(map(int, line.split()))
assert 1 <= t <= 500000
assert 1 <= n <= 500000

assert len(stdin.readline()) == 0
sys.exit(42)
# Nothing to report


