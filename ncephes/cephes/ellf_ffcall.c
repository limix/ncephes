#include "ncephes/ellf.h"

extern double ellie(double phi, double m);
extern double ellik(double phi, double m);
extern double ellpe(double x);
extern double ellpk(double x);

double ncephes_ellie(double phi, double m) { return ellie(phi, m); }
double ncephes_ellik(double phi, double m) { return ellik(phi, m); }
double ncephes_ellpe(double x) { return ellpe(x); }
double ncephes_ellpk(double x) { return ellpk(x); }

