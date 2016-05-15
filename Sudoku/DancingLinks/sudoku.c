/* solve sudoku using Dancing Links
 * Coding by allensll in May 15th,2016
 */
#include <stdio.h>
#include "DLx1.h"

int getRowIndex(int rowNum) {
	int num = rowNum % 9;
	int rowIndex = (rowNum / 9) / 9;
	return 81 + rowIndex * 9 + num;
}

int getColIndex(int rowNum) {
	int num = rowNum % 9;
	int colIndex = (rowNum / 9) % 9;
	return 162 + colIndex * 9 + num;
}

int getSquareIndex(int rowNum) {
	int num = rowNum % 9;
	int rowIndex = (rowNum / 9) / 9;
	int colIndex = (rowNum / 9) % 9;
	int squareIndex = (rowIndex / 3) * 3 + colIndex / 3;
	return 243 + squareIndex * 9 + num;
}

int main () {
	char str[82] = ".................................................................................";
	DLx dlx;
	//81 * 9 = 729
	//81 + 9*9 + 9*9 + 9*9 = 324
	if (!initDLx(&dlx, 729, 324)) {
		return 0;
	}

	int i;
	for (i = 0; i < 729; i++) {
		if (str[i/9] == '.' || str[i/9] - '1' == i % 9) {
			int rowIndex = i;
			int colIndex = i / 9;
			addNode(&dlx, rowIndex, colIndex);
			addNode(&dlx, rowIndex, getRowIndex(i));
			addNode(&dlx, rowIndex, getColIndex(i));
			addNode(&dlx, rowIndex, getSquareIndex(i));
		}
	}
	if (solve(&dlx,0)) {
		int j;
		for (i = 0; i < 81; i++) {
			j = dlx.result[i];
			str[j/9] = '1' + j%9;
		}

		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				printf("%c",str[i*9+j]);
			}
			printf("\n");
		}
	}
	
	gcDLx(&dlx);

	return 0;
}
