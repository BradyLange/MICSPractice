/* 
Problem 6 MICS 2018
Author: Mark Fienup
Finds a single error in each "mathematical mountain".
*/

#include <iostream>
using namespace std;

// Prototypes:
int calcTotalNodes(int numLevels);

int main() {
  int numOfCases, caseNumber;
  int numLevels, totalNodes, i, p, correctSum;

  cin >> numOfCases;
  for (caseNumber = 1; caseNumber <= numOfCases; caseNumber++) {

    // Read next tree
    cin >> numLevels;
    totalNodes = calcTotalNodes(numLevels);
    long * tree = new long [totalNodes];
    for (i = 0; i < totalNodes; i++) {
      cin >> tree[i];
    } // end for (i...

    // iterate non-leaf from root toward leaves 
    for (i = (totalNodes-2) / 2; i >= 0; i--) {
      correctSum = tree[i*2 + 1] + tree[i*2 +2];
      if (tree[i] != correctSum) {
	break;
      } // end if
    } // end for (i...

    if (i > (((totalNodes-2) / 2)-1) / 2) {  // if i on bottom non-leaf level
      p = (i-1)/2;
      if (tree[p*2+1] + tree[p*2+2] == tree[p]) {
	correctSum = tree[i] - tree[i*2+1];
	i = i*2+2;  // right leaf incorrect

      } // end if 

    } // end if

    cout << "WrongCase " << caseNumber << ": " << i << " " << correctSum  << endl;

    delete [] tree;
  } // end for (caseNumber...
 

} // end main

int calcTotalNodes(int numLevels) {
  // avoids math library which might not get linked in on compiling
  int numNodes = 0, nodesPerLevel, level;

  numNodes = 0;
  nodesPerLevel = 1;
  for (level = 1; level <= numLevels; level++) {
    numNodes += nodesPerLevel;
    nodesPerLevel += nodesPerLevel;
  } // end for

  return numNodes;
} // end calcTotalNodes
