/***
 *modify the quicksort algorithm 
 *based on qsort() of Microsoft Corporation's library function
 *Codeing by ALLENSLL
 *Apr 12 2016
 */



#include "stdio.h"
#include "stdlib.h"

int compStr(const void* elem1, const void* elem2);
int compDbl(const void* elem1, const void* elem2);
int compChar(const void* elem1, const void* elem2);
int compInt(const void* elem1, const void* elem2);
void Qsort(void* base, int num, int elemSize,
				int (*comp)(const void*, const void*));
static void swap(char* elem1, char* elem2, int width);
static void shortsort(void* low, void* hight, int elemSize,
				int (*comp)(const void*, const void*));

#define CUTOFF 8
#define STACKSIZE (8*sizeof(void*) - 2)

int compStr(const void* elem1,const void* elem2){
	return strcmp(*(char**)elem1,*(char**)elem2);
}

int compDbl(const void* elem1,const void* elem2){
	return *(double*)elem1 > *(double*)elem2 ? 1:-1;
}

int compChar(const void* elem1,const void* elem2){
	return *(char*)elem1 - *(char*)elem2;
}

int compInt(const void* elem1,const void* elem2){
	return *(int*)elem1 - *(int*)elem2;
}

static void swap (
	char* elem1,
	char* elem2,
	int width
	)
{
	char temp; 
	if (elem1 != elem2) {
		while (width--) {
			temp = *elem1;
			*elem1++ = *elem2;
			*elem2++ = temp;
		}
	}
}


static void shortsort (
	void* low,
	void* hight,
	int elemSize,
	int (*comp)(const void*,const void*)
	)
{
	char* p, *max;
	char* lo = (char*)low;
	char* hi = (char*)hight;
	while (hi > lo) {
		max = lo;
		for (p = lo+elemSize; p <= hi; p += elemSize) {
			if (comp(p, max) > 0) {
				max = p;
			}
		}
		swap(max, hi, elemSize);
		hi -= elemSize;
	}
}

void Qsort(
	void* base,
	int num,
	int elemSize,
	int (*comp)(const void*,const void*)
	)
{
	char* lo, *hi;
	char* mid;
	char* loguy, *higuy;
	int size;
	char* lostack[STACKSIZE], *histack[STACKSIZE];
	int stackptr;

	if (num < 2 || elemSize <= 0) {
		return;
	}

	stackptr = 0;
	lo = (char*)base;//
	hi = (char*)base + elemSize*(num-1);
recurse:
	size = (hi - lo) / elemSize + 1;

	if (size <= CUTOFF) {
		shortsort(lo,hi,elemSize,comp);
	}
	else {
		mid = lo;
		loguy = lo + elemSize;
		higuy = hi;
		for (;;) {
			while (comp(loguy, mid) <= 0 && loguy < hi) {
				loguy += elemSize;
			}
			while (comp(higuy, mid) > 0) {
				higuy -= elemSize;
			}
			if (higuy == lo) {
				loguy = lo + elemSize;
				break;
			}
			if (loguy > higuy) {
				swap(higuy, mid, elemSize);
				higuy -= elemSize;
				break;
			}
			else {
				if (loguy == higuy) {
					if (comp(loguy, mid) < 0) {
						swap(loguy, mid, elemSize);
					}
					else {
						higuy -= elemSize;
						swap(higuy, mid, elemSize);
					}
					higuy -= elemSize;
					break;
				}
			}
			swap(loguy, higuy, elemSize);
		}
		//
		if (higuy-lo >= hi-loguy) {
			if (lo < higuy) {
				lostack[stackptr] = lo;
				histack[stackptr] = higuy;
				++stackptr;
			}
			if (loguy < hi) {
				lo = loguy;
				goto recurse;
			}
		}
		else {
			if (loguy < hi) {
				lostack[stackptr] = loguy;
				histack[stackptr] = hi;
				++stackptr;
			}
			if (lo < higuy) {
				hi = higuy;
				goto recurse;
			}
		}
	}
	--stackptr;
	if (stackptr >= 0) {
		lo = lostack[stackptr];
		hi = histack[stackptr];
		goto recurse;
	}
	else {
		return;
	}
}

int main(){
	int a[50] = {3,2,6,1,9,7,5,2,4,3,3,2,6,1,9,7,5,2,4,3,3,2,6,1,9,7,5,2,4,3,3,2,6,1,9,7,5,2,4,3,3,2,6,1,9,7,5,2,4,3};
	char* s[] = {"bob","allen","jeff"};
	Qsort(a,50,sizeof(int),compInt);
	qsort(s,3,sizeof(char*),compStr);
	int i=0;
	for(i; i<50; i++){
		printf("%d-",a[i]);
	}
	printf("\n");
	i = 0;
	for(i; i<3; i++){
		printf("%s-",s[i]);
	}
	printf("\n");
	return 0;
}
