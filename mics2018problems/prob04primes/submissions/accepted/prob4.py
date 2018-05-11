# prob4.py MICS 2018
# Author:  Mark Fienup
# Generates all the circular primes between two positive integers (max. 500000).

import math

inputLine = input("")
values = inputLine.split()
a = int(values[0])
b = int(values[1])
primesList = []
if a > b:
    temp = a
    a = b
    b = temp

if a == 1:
    a = a + 1
if a == 2:
#    outFile.write(str(a)+"\n")
    a = a + 1

    primesList.append(2)

for i in range(a, 1000000):  # need more than 500000 to check for circular primes 
    prime = True
    for test in range(2,int(math.ceil(math.sqrt(i)))+1):
        if i % test == 0:
            prime = False
            break
    if prime:
        primesList.append(i)

circularPrimes = []

for i in range(len(primesList)):
    prime = primesList[i]
    if prime > b:
        break
    cirPrime = True
    primeStr = str(prime)
    for count in range(1,len(primeStr)):
        nextCircularStr = primeStr[count:] + primeStr[:count]
        nextCircular = int(nextCircularStr)
        if nextCircular not in primesList:
            cirPrime = False
            break
    if cirPrime:
        circularPrimes.append(prime)
for circularPrime in circularPrimes:
    print(circularPrime)
    
# outFile.close()
# inFile.close()
