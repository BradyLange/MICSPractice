""" prob8.py MICS 2018 Highly Recursive Function
    Author:  Mark Fienup
    Solves the highly recursive function using dynamic programming.
    		H(n) = H(n+5) + H(n+4) + H(n+2)  for all value of n <= -8
		H(n) = n for all value of -8 <  n  <  10
		H(n) = H(n-8) + H(n-5) + H(n-3)  for all values of n > 10.
"""

def main():
##    inFile = open('prob8_in.txt', 'r')
##    outFile = open('prob8_out.txt', 'w')
##    numOfCases = int(inFile.readline().strip())
    
    numOfCases = int(input(""))
    for case in range(1, numOfCases+1):
##        n = int(inFile.readline().strip())
        n = int(input(""))
        print("Case %d: H(%d) = %d" % (case, n, H_dynamicProgramming(n)))
##        outFile.write("Case %d: H(%d) = %d\n" % (case, n, H_dynamicProgramming(n)))

def H_dynamicProgramming(n):
    """ Dynamic programming version needed for large values of n """
    
    if -8 < n and n < 10:
        return n
    elif n >= 10:
        H = list(range(0,10))
        for i in range(10, n+1):
            H.append(H[i-8] + H[i-5] + H[i-3])
        return H[n]
    else: # n <= -8 Here I'll use positive index to store H(-index) value
        H = list(range(0,-8,-1))
        for i in range(8, (-n)+1):
            H.append(H[i-5] + H[i-4] + H[i-2])
        return H[-n]
        
        
def H(n):
    """ Recursive version for checking small value of H(n) """
    if n <= -8:
        return H(n+5) + H(n+4) + H(n+2)
    elif -8 < n and n < 10:
        return n
    else:  # n >= 10
        return H(n-8) + H(n-5) + H(n-3)
        
main()
