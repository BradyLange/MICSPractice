""" Problem 3 MICS 2018 Invisible Ink Encryption program for data file"""

def main():
##    inFile = open("prob3_in.txt")
##    msg = inFile.read().strip("\n")
    msg = input("")
    charCnt = len(msg) // 7
    decryptedStr = ""
    
    for count in range(charCnt):
        charStr = msg[count*7 : (count+1)*7]
##        print(charStr)
        charASCII = 0
        for char in charStr:
            if char == '\t':
                charASCII = charASCII * 2 + 1
            else:
                charASCII *= 2
        #print(chr(charASCII), charASCII)
        decryptedStr += chr(charASCII)
##    print(decryptedStr)
##    outFile = open("prob3_out.txt", "w")
##    outFile.write(decryptedStr)
    print(decryptedStr)
main()
    

