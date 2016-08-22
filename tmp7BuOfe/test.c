
#include <stdio.h>
#include "ncephes/cprob.h"

int main()
{
  printf("incbet: %.3f", ncephes_incbet(1., 3., 0.3));
  return 0;
}
