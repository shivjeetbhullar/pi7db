#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char** myprint(char **or,int arlen)
{

    int i = 0;
  static char **orderedIds;
  orderedIds = malloc(arlen * sizeof(char*));
  do{
  char * buffer = 0;
long length;
FILE * f = fopen (or[i], "rb");

if (f)
{
  fseek (f, 0, SEEK_END);
  length = ftell (f);
  fseek (f, 0, SEEK_SET);
  buffer = malloc (length);
  if (buffer)
  {
    fread(buffer, 1, length, f);
  }
  fclose (f);
}

if (buffer)
{
  orderedIds[i] = buffer;
//  printf("%s",buffer);
}      
    i++;
   }while(i<arlen);

 return orderedIds;
}


