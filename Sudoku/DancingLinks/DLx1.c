#include <stdio.h>
#include <stdlib.h>
#include "DLx1.h"

int initDLx(DLx *pDLx, int rowNum, int colNum) {
	if (!(pDLx->nodes = (Node*)malloc(sizeof(Node) * rowNum * colNum))) {
		return 0;
	}
	if (!(pDLx->row = (Node*)malloc(sizeof(Node) * (rowNum)))) {
		return 0;
	}
	if (!(pDLx->col = (Node*)malloc(sizeof(Node) * (colNum +1)))) {
		return 0;
	}
	if (!(pDLx->result = (int*)malloc(sizeof(int) * rowNum))) {
		return 0;
	}

	int i = 0;
	for (i = 0; i <= colNum; i++) {
		pDLx->col[i].up = pDLx->col[i].down = pDLx->col + i;		
		pDLx->col[i].left = pDLx->col + (i+colNum) % (1+colNum);
		pDLx->col[i].right = pDLx->col + (i+1) % (1+colNum);
		pDLx->col[i].colRoot = pDLx->col + i;
		pDLx->col[i].sumOfCol = 0;
		pDLx->col[i].row = 0;           //no use
	}
	for (i = 0; i < rowNum; i++) {
		pDLx->row[i].up = pDLx->row[i].down = pDLx->row[i].colRoot = pDLx->row + i;
		pDLx->row[i].left = pDLx->row[i].right = pDLx->row + i;
		pDLx->row[i].sumOfCol = 0;  //no use
		pDLx->row[i].row = i;  // no use
	}
	pDLx->head = pDLx->col + colNum;
	pDLx->nodeCount = 0;
	return 1;
}
void addNode(DLx *pDLx, int row, int col) {
	pDLx->nodes[pDLx->nodeCount].up = pDLx->col[col].up;
	pDLx->nodes[pDLx->nodeCount].down = pDLx->col + col;
	pDLx->nodes[pDLx->nodeCount].left = pDLx->row[row].left;
	pDLx->nodes[pDLx->nodeCount].right = pDLx->row + row;
	pDLx->nodes[pDLx->nodeCount].row = row;
	pDLx->nodes[pDLx->nodeCount].colRoot = pDLx->col + col;

	pDLx->col[col].up = pDLx->col[col].up->down = pDLx->nodes + pDLx->nodeCount;
	pDLx->row[row].left = pDLx->row[row].left->right = pDLx->nodes + pDLx->nodeCount;
	pDLx->nodeCount++;
	pDLx->col[col].sumOfCol++;
}

void cover(Node *colRoot) {
	Node *p, *q;
	colRoot->left->right = colRoot->right;
	colRoot->right->left = colRoot->left;
	for (p = colRoot->down; p != colRoot; p = p->down) {
		for (q = p->right; q != p; q = q->right) {
			q->up->down = q->down;
			q->down->up = q->up;
			q->colRoot->sumOfCol--;
		}
	}
}

void uncover(Node *colRoot) {
	Node *p, *q;
	colRoot->left->right = colRoot->right->left = colRoot;
	for (p = colRoot->down; p != colRoot; p = p->down) {
		for (q = p->right; q != p; q = q->right) {
			q->down->up = q->up->down = q;
			q->colRoot->sumOfCol++;
		}
	}
}

Node* findMinCol(DLx *pDLx) {
	Node *pMin, *p, *q;
	for(pMin = pDLx->head->right,p = pMin->right; p != pDLx->head; p = p->right) {
		if ((pMin->sumOfCol) > (p->sumOfCol)) {
			pMin = p;
		}
	}
	return pMin;
}

int solve(DLx *pDLx, int k) {
	if (pDLx->head->right == pDLx->head) {
		pDLx->resultCount = k;
		return 1;
	}

	Node *pMin, *p, *q;
	pMin = findMinCol(pDLx);

	cover(pMin);

	for (p = pMin->down; p != pMin; p = p->down) {
		pDLx->result[k] = p->row;
		for (q = p->right; q != p; q=q->right) {
			cover(q->colRoot);
		}
		if (solve(pDLx,k+1)) {
			return 1;
		}
		for (q = p->left; q != p; q = q->left) {
			uncover(q->colRoot);
		}
	}

	uncover(pMin);
	return 0;
}

void gcDLx(DLx *pDLx) {
	free(pDLx->nodes);
	free(pDLx->row);
	free(pDLx->col);
	free(pDLx->result);	
}

