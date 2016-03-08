/* Huffman Encoder
   This is an simple demo of Huffman encode
   Coding by ALLENSLL in Jul 9th,2014
   Add English comments in Mar 8th,2016
   */

#include<stdio.h>
#include<stdlib.h>
typedef char *HuffmanCode;
char infile[50]={0};
char outfile[50]={0};

typedef struct {	//node structure contains three pointers to store binary tree
	int CodeNumber;
	int Frequency;
	int parent,lchild,rchild;
} HTNode;

typedef struct node{	//storage Huffman codes useing list 
	char elem;
	struct node *next;
}LNode, *LinkNode;

int Instraction(); //a simple starting UI
int CreateList( int list[127] ); //traversal the source file,establish a frequency table based ASCII
int Select( int copy[253], int *x, int *y, int *w ); //elect two smallest weight to code
int HuffmanCoding( int list[127] ); //create Huffman tree
int PrintH( HTNode HuffmanTree[253] ); //print Huffman tree
int PrintC( HTNode HuffmanTree[253] ); //encoding

int Instraction()
{
	printf("	**************************************************\n");
	printf("	                Huffman Encoder                   \n");
	printf("	          (Only support ASCII format£©            \n");
	printf("	**************************************************\n");
	printf("\nGo with Enter key:");
	getchar();
	return 0;
}

int CreateList( int list[127] )
{
	FILE *fp;
	int frequency;
	
	printf("Please input file:");
	scanf("%s",infile);

	if((fp=fopen(infile,"r"))==NULL)
	{
		printf("cannot open file\n");
		exit(0);
	}

	while (1) {
		frequency = (int)fgetc(fp);
		if (!feof(fp)) {
			list[frequency]++;
		}
		else {
			break;
		}
	}

//	while(!feof(fp))
//	{
//		frequency=(int)fgetc(fp);
//		printf("\n%d",frequency);
//		list[frequency]++;
//	}
	fclose(fp);
	return 0;
}

int Select ( int copy[253], int *min1, int *min2, int *weight )
{
	int i,tag=0, num1=0, num2=0;

	for( i=0; i<253; i++ )
	{
		if( copy[i]!=0 )
		{
			*min1=copy[i];
			num1=i;
			break;
		}

	}
	for( i=0; i<253; i++ )
	{
		if( copy[i]!=0 )
		{
			if( *min1>copy[i] )
			{
				*min1=copy[i];
				num1=i;
			}
		}
	}
	copy[num1]=0; //first

	for( i=0; i<253; i++ )
	{
		if( copy[i]!=0 )
		{
			tag=1;
			*min2=copy[i];
			num2=i;
			break;
		}
	}
	for( i; i<253; i++)
	{
		if( copy[i]!=0 )
		{
			if( *min2>copy[i] )
			{
				*min2=copy[i];
				num2=i;
			}
		}
	}
	copy[num2]=0; //second

	*weight = *min1 + *min2; //new weight
	*min1=num1;
	*min2=num2;
	if( tag==0 ) {
		*weight=0;
	}
	return 0;
}

int PrintH( HTNode HuffmanTree[253] )
{
	FILE *fp1;
	int i;

	for( i=0; infile[i]!='\0'; i++ ) {
		outfile[i] = infile[i];
	}
	outfile[i++]='_';
	outfile[i++]='H';
	outfile[i++]='u';
	outfile[i++]='f';
	outfile[i++]='f';
	outfile[i++]='m';
	outfile[i++]='a';
	outfile[i++]='n';

	if((fp1=fopen(outfile,"w"))==NULL)
	{
		printf("cannot open file\n");
		exit(0);
	}

//	fprintf(fp1,"frequency\tparent\tlchild\trchild\taddress\tASCII\t\n");
	for( i=0; i<253; i++ )
	{
		fprintf(fp1,"%d\t\t%d\t%d\t%d\t%d\t%d\t\n", HuffmanTree[i].Frequency, HuffmanTree[i].parent, HuffmanTree[i].lchild, HuffmanTree[i].rchild, i, HuffmanTree[i].CodeNumber );
	}

	fclose(fp1);
	return 0;
}

int PrintC( HTNode HuffmanTree[253] )
{
	FILE *fp1 , *fp2;
	LinkNode p, q;
	int address[127]={0}; 
	int i,j,f;
	LNode HC[127]={0};  

	for( i=0; i<127; i++ )
	{
		address[i] = -2;
	}
	for( i=0; i<127; i++ )
	{
		HC[i].elem = '\0';
		HC[i].next = NULL;
	}
	
	for( i=0; i<127; i++ )
	{
		if( HuffmanTree[i].CodeNumber!=-2 )
		{
			address[HuffmanTree[i].CodeNumber] =i;
		}
	}  //initialize
	
	for( i=0; i<127; i++ )
	{
		if( (HuffmanTree[address[i]].lchild != -2) || (HuffmanTree[address[i]].rchild != -2)) {
			continue;
		}
		q=NULL;
		j=address[i] ;
		f=HuffmanTree[j].parent;
		while( f!=-1 ) {
			p=(LinkNode)malloc(sizeof(LNode));
			p->next =q;
			if( HuffmanTree[f].lchild == j ) {
				p->elem ='0';
			}
			else {
				p->elem ='1';
			}
			q=p;
			j=f;
			f=HuffmanTree[f].parent;
		}
		if( HuffmanTree[f].lchild == j ) {
			HC[i].elem ='0';
		}
		else {
			HC[i].elem ='1';
		}
		HC[i].next = q;
	}  //Up coding from the leaf node£¬inserted one by one from the list header

	if((fp1=fopen(outfile,"a"))==NULL)
	{
		printf("cannot open file\n");
		exit(0);
	}
	if((fp2=fopen(infile,"r"))==NULL)
	{
		printf("cannot open file\n");
		exit(0);
	}
	
/*	for(i=0;i<127;i++)  //print codes
	{
		p=&HC[i];
		if(p->elem !=NULL) {
		do {
			printf("%c",p->elem );
			p=p->next ;
		} while( p!=NULL);
		printf("\n");
		}
	} */

	i=(int)fgetc(fp2); // *******
	while( !feof(fp2) ) {	
		
		p=&HC[i];
		if(p->elem != '\0') {
			do {
				fprintf(fp1,"%c",p->elem );
				p=p->next;
			} while( p != NULL );
		}
		i=(int)fgetc(fp2);
	}  //individually coded using the coded list
	printf("\nsucceed\n");
	fclose(fp1);
	fclose(fp2);
	return 0;
}

int HuffmanCoding( int list[127] )
{
	int i, j=0, min1, min2, weight, copy[253]={0};
	HTNode HuffmanTree[253]={0};

	for( i=0; i<253; i++ )
	{
		HuffmanTree[i].CodeNumber = -2;
		HuffmanTree[i].lchild = -2;
		HuffmanTree[i].rchild = -2;
	}
	
	for( i=1; i<127; i++ )
	{
		if( list[i]!=0 )
		{
			HuffmanTree[j].CodeNumber = i;
			HuffmanTree[j].Frequency = list[i];
			j++;
		}
	}  //initialize

	for( i=0; HuffmanTree[i].Frequency!=0; i++ )
	{
		copy[i] = HuffmanTree[i].Frequency;
	}

	for( i; i<127; i++ )
	{
		Select ( copy, &min1, &min2, &weight );
		if( weight!=0)
		{
			HuffmanTree[j].Frequency = weight;
			HuffmanTree[min1].parent = j;
			HuffmanTree[j].lchild  = min1;
			HuffmanTree[min2].parent = j;
			HuffmanTree[j].rchild = min2;
			copy[j] = weight;
			j++;
		}  //build Huffman tree
		else {
			HuffmanTree[min1].parent = -1;
			break;
		}
	}
	PrintH( HuffmanTree );  //print Huffman tree

	PrintC( HuffmanTree );  //coding

	return 0;
}

int main()
{
	int list[127]={0};

	Instraction();
	CreateList( list );
	HuffmanCoding( list );
	return 0;
}
