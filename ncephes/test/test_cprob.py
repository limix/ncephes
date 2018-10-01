from __future__ import unicode_literals

from numpy.testing import assert_almost_equal

from ncephes import (
    bdtr,
    bdtrc,
    bdtri,
    btdtr,
    gamma,
    chdtr,
    chdtrc,
    chdtri,
    cosm1,
    erf,
    erfc,
    expm1,
    expx2,
    fdtr,
    fdtrc,
    fdtri,
    gdtr,
    gdtrc,
    igam,
    igamc,
    incbet,
    incbi,
    kolmogi,
    kolmogorov,
    lgam,
    log1p,
    nbdtr,
    nbdtrc,
    nbdtri,
    ndtr,
    ndtri,
    pdtr,
    pdtrc,
    pdtri,
    smirnov,
    smirnovi,
    stdtr,
    stdtri,
)


def test_bdtr():
    assert_almost_equal(bdtr(4, 5, 0.25), 0.9990234375000000)
    assert_almost_equal(bdtrc(4, 5, 0.25), 0.0009765625000000)
    assert_almost_equal(bdtri(4, 5, 0.25), 0.9440875112949020)


def test_btdtr():
    assert_almost_equal(btdtr(4, 5, 0.25), 0.1138153076171875)


def test_chdtr():
    assert_almost_equal(chdtr(4, 5), 0.7127025048163542)
    assert_almost_equal(chdtrc(4, 5), 0.2872974951836458)
    assert_almost_equal(chdtri(4, 0.3), 4.8784329665604087)


def test_expx2():
    assert_almost_equal(expx2(1, 2), 2.7182818284590451)


def test_fdtr():
    assert_almost_equal(fdtr(4, 5, 0.3), 0.1333536247071635)
    assert_almost_equal(fdtrc(4, 5, 0.3), 0.8666463752928364)
    assert_almost_equal(fdtri(4, 5, 0.3), 0.564931901511857)


def test_gamma():
    assert_almost_equal(gamma(1.5), 0.8862269254527579)
    assert_almost_equal(lgam(3.4), 1.0923280598027414)


def test_gdtr():
    assert_almost_equal(gdtr(1, 2, 0.1), 0.0046788401604445)
    assert_almost_equal(gdtrc(1, 2, 0.1), 0.9953211598395555)


def test_igam():
    assert_almost_equal(igam(1, 2), 0.8646647167633873)
    assert_almost_equal(igamc(2, 1), 0.7357588823428847)


def test_incbet():
    assert_almost_equal(incbet(1., 3., 0.3), 0.657)


def test_incbi():
    assert_almost_equal(incbi(1., 3., 0.3), 0.1120959982573993)


def test_kolmogorov():
    assert_almost_equal(smirnov(2, 0.3), 0.61)
    assert_almost_equal(kolmogorov(2), 0.00067092525578)
    assert_almost_equal(smirnovi(2, 0.3), 0.474679434488)
    assert_almost_equal(kolmogi(0.24), 1.02920479826)


def test_nbdtr():
    assert_almost_equal(nbdtr(1, 3, 0.5), 0.3125)
    assert_almost_equal(nbdtrc(1, 3, 0.5), 0.6875)
    assert_almost_equal(nbdtri(1, 3, 0.5), 0.614272431868)


def test_ndtr():
    assert_almost_equal(ndtr(0.3), 0.617911422189)
    assert_almost_equal(erf(1.3), 0.9340079449406524)
    assert_almost_equal(erfc(0.3), 0.671373240541)


def test_ndtri():
    assert_almost_equal(ndtri(0.6), 0.253347103136)


def test_pdtr():
    assert_almost_equal(pdtr(2, 0.15), 0.999497137624)
    assert_almost_equal(pdtrc(2, 0.15), 0.000502862376402)
    assert_almost_equal(pdtri(2, 0.15), 4.72305156339)


def test_stdtr():
    assert_almost_equal(stdtr(2, 3), 0.952267016867)
    assert_almost_equal(stdtri(5, 0.1), -1.47588404882)


def test_unity():
    assert_almost_equal(log1p(0.1), 0.0953101798043)
    assert_almost_equal(expm1(0.5), 0.6487212707)
    assert_almost_equal(cosm1(0.9), -0.378390031729)
