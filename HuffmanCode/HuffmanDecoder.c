/* Huffman Decoder
   This is an simple demo of Huffman encode
   Coding by ALLENSLL in Jul 9th,2014
   Add English comments in Mar 8th,2016
   */
   
#include<stdio.h>
#include<stdlib.h>
typedef char *HuffmanCode;
char infile[50]={0};
char outfile[50]={0};

typedef struct {
	int CodeNumber;
	int Frequency;
	int parent,lchild,rchild;
} HTNode;

int Instraction(); //a simple starting UI
int DecodeH( HTNode HuffmanTree[253] ); //decode

int Instraction()
{
	printf("	**************************************************\n");
	printf("	                Huffman Decoder                   \n");
	printf("	          (Only support ASCII format)             \n");
	printf("	**************************************************\n");
	printf("\nGo with Enter key:");
	getchar();
	return 0;
}

int DecodeH( HTNode HuffmanTree[253] )
{
	FILE *fp1,*fp2;
	int i,j,head;
	char ch;
	
	printf("Please input file:");
	scanf("%s",infile);

	if((fp1=fopen(infile,"r"))==NULL)
	{
		printf("cannot open file\n");
		exit(0);
	}
	for( i=0; i<253; i++ )
	{
		fscanf(fp1,"%d\t\t%d\t%d\t%d\t%d\t%d\t\n", &HuffmanTree[i].Frequency, &HuffmanTree[i].parent, &HuffmanTree[i].lchild, &HuffmanTree[i].rchild, &i, &HuffmanTree[i].CodeNumber );
	}  //create Huffman tree

	for( i=0; infile[i]!='_'; i++ ) {
		outfile[i] = infile[i];
	}
	outfile[i++]='#';
	outfile[i++]='\0';

	if((fp2=fopen(outfile,"w"))==NULL)
	{
		printf("cannot open file\n");
		exit(0);
	}

	for( i=0; i<253; i++)
	{
		if( HuffmanTree[i].parent == -1 )
			j=head=i;
	} //find the root
	
	ch = fgetc(fp1);
	while(!feof(fp1))
	{
		ch=fgetc(fp1);
	//	if (!feof(fp1)) {

		if( ch == '0' ) {
			i=HuffmanTree[j].lchild ;
			if( HuffmanTree[j].CodeNumber != -2 ) {
				fprintf(fp2,"%c",(char)HuffmanTree[j].CodeNumber);
				j=head;
			}
			else {
				j=HuffmanTree[j].lchild ;
			}
		}
		else {
			i=HuffmanTree[j].rchild ;
			if( HuffmanTree[j].CodeNumber != -2 ) {
				fprintf(fp2,"%c",(char)HuffmanTree[j].CodeNumber);
				j=head;
			}
			else {
				j=HuffmanTree[j].rchild ;
			}
		}
	}  //decode
	printf("\nSucceed\n");
	fclose(fp2);
	return 0;
}

int main()
{
	HTNode HuffmanTree[253]={0};

	Instraction();
	DecodeH( HuffmanTree );
	return 0;
}
