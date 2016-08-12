from numpy.testing import assert_almost_equal

from ncephes import ellf


def test_ellie():
    assert_almost_equal(ellf.ellie(-5.3, 0.12), -5.12290521194)


def test_ellik():
    assert_almost_equal(ellf.ellik(-5.3, 0.12), -5.48607395126)


def test_ellpe():
    assert_almost_equal(ellf.ellpe(0.12), 1.120741662164857)


def test_ellpk():
    assert_almost_equal(ellf.ellpk(0.12), 2.492635323239716)
