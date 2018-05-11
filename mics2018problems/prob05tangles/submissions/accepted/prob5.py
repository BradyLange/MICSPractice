# prob5.py MICS 2018 Wreck Tangles.

def main():
##    inFile = open('prob5_in.txt', 'r')
##    outFile = open('prob5_out.txt', 'w')
##    numOfCases = int(inFile.readline().strip())
    
    numOfCases = int(input(""))
    for case in range(1, numOfCases+1):
##        NWord = inFile.readline().strip()
##        EWord = inFile.readline().strip()
##        SWord = inFile.readline().strip()
##        WWord = inFile.readline().strip()
        NWord = input("")
        EWord = input("")
        SWord = input("")
        WWord = input("")
        NEMatches = wordIntersects(NWord, range(2,len(NWord)), EWord, range(len(EWord)-2))
        #print(NEMatches)
        SEMatches = wordIntersects(SWord, range(2,len(SWord)), EWord, range(2,len(EWord)))
        #print(SEMatches)
        NWMatches = wordIntersects(NWord, range(len(NWord)-2), WWord, range(len(WWord)-2))
        #print(NWMatches)
        SWMatches = wordIntersects(SWord, range(len(SWord)-2), WWord, range(2, len(WWord)))
        #print(SWMatches)
        NDists = [] #list of [N word dist, W index, E index]
        for NWmatch in NWMatches:
            for NEmatch in NEMatches:
                NDist = NEmatch[0] - NWmatch[0] 
                if NDist > 1:
                    NDists.append([NDist, NWmatch[1], NEmatch[1]])
        SDists = [] #list of [S word dist, W index, E index]
                
        for SWmatch in SWMatches:
            for SEmatch in SEMatches:
                SDist = SEmatch[0] - SWmatch[0] 
                if SDist > 1:
                    SDists.append([SDist, SWmatch[1], SEmatch[1]])
                
        #print(NDists)
        #print(SDists)

        wreckList = [] #list of [Size, W index of N, E index of N, W index of S, E index of S]
                
        for NDist in NDists:
            for SDist in SDists:
                if NDist[0] == SDist[0]:
                    WDist = SDist[1] - NDist[1]
                    EDist = SDist[2] - NDist[2]
                    if WDist == EDist and WDist > 1:
                        wreckList.append((NDist[0]-1) * (WDist-1))  
        print("Case %d: %d" % (case, len(wreckList)))
##        outFile.write("Case %d: %d\n" % (case, len(wreckList)))

        
def wordIntersects(wordA, iterA, wordB, iterB):
    intersects = []
    for a in iterA:
        for b in iterB:
            if wordA[a] == wordB[b]:
                intersects.append([a,b])
    return intersects

main()
