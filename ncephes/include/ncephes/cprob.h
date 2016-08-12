#ifndef CPROB_H
#define CPROB_H

extern double ncephes_bdtrc(int k, int n, double p);
extern double ncephes_bdtr(int k, int n, double p);
extern double ncephes_bdtri(int k, int n, double y);
extern double ncephes_btdtr(double a, double b, double x);
extern double ncephes_chdtrc(double df, double x);
extern double ncephes_chdtr(double df, double x);
extern double ncephes_chdtri(double df, double y);
extern double ncephes_expx2(double x, int sign);
extern double ncephes_fdtrc(int ia, int ib, double x);
extern double ncephes_fdtr(int ia, int ib, double x);
extern double ncephes_fdtri(int ia, int ib, double y);
extern double ncephes_cephes_gamma(double x);
extern double ncephes_lgam(double x);
extern double ncephes_gdtr(double a, double b, double x);
extern double ncephes_gdtrc(double a, double b, double x);
extern double ncephes_igamc(double a, double x);
extern double ncephes_igam(double a, double x);
extern double ncephes_igami(double a, double y0);
extern double ncephes_incbet(double aa, double bb, double xx);
extern double ncephes_incbi(double aa, double bb, double yy0);
extern double ncephes_smirnov(int n, double e);
extern double ncephes_kolmogorov(double y);
extern double ncephes_smirnovi(int n, double p);
extern double ncephes_kolmogi(double p);
extern double ncephes_nbdtrc(int k, int n, double p);
extern double ncephes_nbdtr(int k, int n, double p);
extern double ncephes_nbdtri(int k, int n, double p);
extern double ncephes_ndtr(double a);
extern double ncephes_erfc(double a);
extern double ncephes_erf(double x);
extern double ncephes_ndtri(double y0);
extern double ncephes_pdtrc(int k, double m);
extern double ncephes_pdtr(int k, double m);
extern double ncephes_pdtri(int k, double y);
extern double ncephes_stdtr(int k, double t);
extern double ncephes_stdtri(int k, double p);
extern double ncephes_log1p(double x);
extern double ncephes_expm1(double x);
extern double ncephes_cosm1(double x);

#endif
