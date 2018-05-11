""" Problem 2 MICS 2018 Circus Sort"""

def main():
    numOfPts = int(input(""))
##    inFile = open("prob2.in")
##    numOfPts = int(inFile.readline().strip())
    pts = []

##    ptStr = inFile.readline()
    ptStr = input("").strip()
    coordList = ptStr.split()
    
    for pt in range(numOfPts):
        pts.append((float(coordList[2*pt]), float(coordList[2*pt+1])))
##        ptStr = input("Enter x, y point: ")
##        pts.append((float(ptStr.split()[0]), float(ptStr.split()[1])))
##    print(pts)
    pts.sort()
##    print(pts)

    ring1pts, ring2pts, ring3pts = partitionPtsToRings(pts)
##    print(ring1pts)
##    print(ring2pts)
##    print(ring3pts)

    sortedRing1pts = clockwiseSort(ring1pts)
    print("Ring 1:", end="")
    for pt in sortedRing1pts:
        print(" (%.1f,%.1f)" % pt, end="")
    print()
    sortedRing2pts = clockwiseSort(ring2pts)
    print("Ring 2:", end="")
    for pt in sortedRing2pts:
        print(" (%.1f,%.1f)" % pt, end="")
    print()
    sortedRing3pts = clockwiseSort(ring3pts)
    print("Ring 3:", end="")
    for pt in sortedRing3pts:
        print(" (%.1f,%.1f)" % pt, end="")
    print()

def clockwiseSort(ringPts):
    ptsOnOrAbove = []
    ptsBelow = []
    for pt in ringPts:
        if pt[1] < 0.0:
            ptsBelow.append(pt)
        else:
            ptsOnOrAbove.append(pt)
    ptsBelow.reverse()
    ptsOnOrAbove.extend(ptsBelow)
    return ptsOnOrAbove

def partitionPtsToRings(pts):
    ring1pts = []
    ring2pts = []

    xIntersectCount = 1
    ring1pts.append(pts.pop(0))
    while xIntersectCount < 2:
        nextPt = pts.pop(0)
        ring1pts.append(nextPt)
        if nextPt[1] == 0.0:
            xIntersectCount += 1
        
    xIntersectCount = 1
    ring2pts.append(pts.pop(0))
    while xIntersectCount < 2:
        nextPt = pts.pop(0)
        ring2pts.append(nextPt)
        if nextPt[1] == 0.0:
            xIntersectCount += 1
        
    ring3pts = pts

    return ring1pts, ring2pts, ring3pts


main()
    

