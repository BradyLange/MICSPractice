#!/usr/bin/env python3
# input format check for Problem 5
# Sample input
# 1 
# dragon 
# antelope 
# eagle 
# badger 

from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"
decimal =  "[-+]?[0-9]*\.?[0-9]+"
word = "[-a-z]+"
oneint = re.compile(integer + "\n")
oneword = re.compile(word + "\n")

# read in the first line which is the number of scaling factors
line = stdin.readline()
assert oneint.match(line)
n = int(line)
assert n > 0
n = n * 4

# read each line and check if it is a legal scale factor
for i in range(n):
   line = stdin.readline()
   #print ("checking line: " , line)
   assert oneword.match(line)

#assert len(stdin.readline()) == 0
#Ssys.exit(42)
# Nothing to report
