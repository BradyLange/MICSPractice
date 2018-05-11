""" Problem 1 MICS 2018 ASCII art of CSS """

def main():
    #numOfCases = int(input("Enter number of cases: "))
    numOfCases = int(input(""))

    for case in range(1, numOfCases+1):
        scale = int(input(""))
        print("Case "+str(case)+":")
        printCSS(scale)

def printCSS(scale):
    letterDim = scale * 5

    for count in range(scale):
        print("C"*letterDim + " "*letterDim + "S"*letterDim + " "*letterDim + "S"*letterDim)
        
    for count in range(scale):
        print("C"*scale + " "*(2*letterDim-scale) + "S"*scale + " "*(2*letterDim-scale) + "S"*scale + " "*(letterDim-scale))

    for count in range(scale):
        print("C"*scale + " "*(2*letterDim-scale) + "S"*letterDim + " "*letterDim + "S"*letterDim)
        
    for count in range(scale):
        print("C"*scale + " "*(2*letterDim-scale) + " "*(letterDim-scale)+ "S"*scale + " "*(2*letterDim-scale)+ "S"*scale)

    for count in range(scale):
        print("C"*letterDim + " "*letterDim + "S"*letterDim + " "*letterDim + "S"*letterDim)

    print('\n'*4)

main()
    

