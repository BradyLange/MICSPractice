/* Problem 7 MICS 2018 - The Plot Thickens
   Author:  Mark Fienup
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
	
  // Note that there is no "prompt for input" cout
  int caseNumber, numberOfCases, numberOfRects, canvasWidth, canvasHeight;
  int x, y, row, col, i, width, height, count1s;
  int * canvas;

  scanf("%d", &numberOfCases);
  for(caseNumber = 1; caseNumber <= numberOfCases; caseNumber++) {
    scanf("%d", &canvasWidth);
    scanf("%d", &canvasHeight);
    scanf("%d", &numberOfRects);
    canvas = calloc(canvasWidth*canvasHeight, sizeof(int)); // embed 2D array into single 1D array
    for (i = 0; i < numberOfRects; i++) {
      scanf("%d", &x);
      scanf("%d", &y);
      scanf("%d", &width);
      scanf("%d", &height);
      for (col = 0; col < width; col++) {
	     for (row = 0; row < height; row++) {
	        *(canvas + (y + row)*canvasWidth + (x+col)) += 1;
	     } // end for (row ...
      } // end for (col ...
      /*
      printf("after rectangle %d\n", i);
      for (x = 0; x < canvasWidth*canvasHeight; x++) {
	if (x % canvasWidth == 0) {
	  printf("\n");
	} // end if
	printf("%d ", canvas[x]);
      } // end for (i ...
      printf("\n");
      */
      
    } // end for (i ...
    count1s = 0;
    for (i = 0; i < canvasWidth*canvasHeight; i++) {
      if (canvas[i] % 2 == 1) {
	     count1s += 1;
      } // end if
    } // end for (i ...
    printf("Case %d: %d\n", caseNumber, count1s);
    free(canvas);
  } // end for
  return 0;
}
