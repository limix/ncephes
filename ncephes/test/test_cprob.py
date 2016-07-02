from .. import cprob
import unittest

class TestCprob(unittest.TestCase):
    def test_bdtr(self):
        self.assertAlmostEqual(cprob.bdtr(4, 5, 0.25), 0.9990234375000000)
        self.assertAlmostEqual(cprob.bdtrc(4, 5, 0.25), 0.0009765625000000)
        self.assertAlmostEqual(cprob.bdtri(4, 5, 0.25), 0.9440875112949020)

    def test_btdtr(self):
        self.assertAlmostEqual(cprob.btdtr(4, 5, 0.25), 0.1138153076171875)

    def test_chdtr(self):
        self.assertAlmostEqual(cprob.chdtr(4, 5), 0.7127025048163542)
        self.assertAlmostEqual(cprob.chdtrc(4, 5), 0.2872974951836458)
        self.assertAlmostEqual(cprob.chdtri(4, 0.3), 4.8784329665604087)

    def test_expx2(self):
        self.assertAlmostEqual(cprob.expx2(1, 2), 2.7182818284590451)

    def test_fdtr(self):
        self.assertAlmostEqual(cprob.fdtr(4, 5, 0.3), 0.1333536247071635)
        self.assertAlmostEqual(cprob.fdtrc(4, 5, 0.3), 0.8666463752928364)
        self.assertAlmostEqual(cprob.fdtri(4, 5, 0.3), 1.6286329978911640)

    def test_gamma(self):
        self.assertAlmostEqual(cprob.cephes_gamma(1.5), 0.8862269254527579)
        self.assertAlmostEqual(cprob.lgam(3.4), 1.0923280598027414)

    def test_gdtr(self):
        self.assertAlmostEqual(cprob.gdtr(1, 2, 0.1), 0.0046788401604445)
        self.assertAlmostEqual(cprob.gdtrc(1, 2, 0.1), 0.9953211598395555)

    def test_igam(self):
        self.assertAlmostEqual(cprob.igam(1, 2), 0.8646647167633873)
        self.assertAlmostEqual(cprob.igamc(2, 1), 0.7357588823428847)

    def test_incbet(self):
        self.assertAlmostEqual(cprob.incbet(1., 3., 0.3), 0.657)

    def test_incbi(self):
        self.assertAlmostEqual(cprob.incbi(1., 3., 0.3), 0.1120959982573993)

    def test_kolmogorov(self):
        self.assertAlmostEqual(cprob.smirnov(2, 0.3), 0.61)
        self.assertAlmostEqual(cprob.kolmogorov(2), 0.00067092525578)
        self.assertAlmostEqual(cprob.smirnovi(2, 0.3), 0.474679434488)
        self.assertAlmostEqual(cprob.kolmogi(0.24), 1.02920479826)

    def test_nbdtr(self):
        self.assertAlmostEqual(cprob.nbdtr(1, 3, 0.5), 0.3125)
        self.assertAlmostEqual(cprob.nbdtrc(1, 3, 0.5), 0.6875)
        self.assertAlmostEqual(cprob.nbdtri(1, 3, 0.5), 0.614272431868)

    def test_ndtr(self):
        self.assertAlmostEqual(cprob.ndtr(0.3), 0.617911422189)
        self.assertAlmostEqual(cprob.erf(1.3), 0.9340079449406524)
        self.assertAlmostEqual(cprob.erfc(0.3), 0.671373240541)

    def test_ndtri(self):
        self.assertAlmostEqual(cprob.ndtri(0.6), 0.253347103136)

    def test_pdtr(self):
        self.assertAlmostEqual(cprob.pdtr(2, 0.15), 0.999497137624)
        self.assertAlmostEqual(cprob.pdtrc(2, 0.15), 0.000502862376402)
        self.assertAlmostEqual(cprob.pdtri(2, 0.15), 4.72305156339)

    def test_stdtr(self):
        self.assertAlmostEqual(cprob.stdtr(2, 3), 0.952267016867)
        self.assertAlmostEqual(cprob.stdtri(5, 0.1), -1.47588404882)

    def test_unity(self):
        self.assertAlmostEqual(cprob.log1p(0.1), 0.0953101798043)
        self.assertAlmostEqual(cprob.expm1(0.5), 0.6487212707)
        self.assertAlmostEqual(cprob.cosm1(0.9), -0.378390031729)

if __name__ == '__main__':
    unittest.main()
