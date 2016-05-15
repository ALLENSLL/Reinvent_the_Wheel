//#include <DLx1.c>
#ifndef _DLx1_H
#define _DLx1_H

typedef struct Node {
	struct Node *up;
	struct Node *down;
	struct Node *left;
	struct Node *right;
	struct Node *colRoot;
	int row;
	int sumOfCol;
} Node;

typedef struct DLx {
	Node *nodes;
	Node *row;
	Node *col;
	Node *head;
	int rowNum;
	int colNum;
	int nodeCount;
	int *result;
	int resultCount;
} DLx;

int initDLx(DLx *pDLx, int rowNum, int colNum);
void addNode(DLx *pDLx, int row, int col);
void cover(Node *colRoot);
void uncover(Node *colRoot);
//Node* findMinCol(DLx *pDLx);
int solve(DLx *pDLx, int resultCount);
void gcDLx(DLx *pDLx);

#endif
