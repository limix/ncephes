#include <stdio.h>
#include "ncephes/cprob.h"

double minus_incbet(double a, double b, double c)
{
    return -ncephes_incbet(a, b, c);
}
