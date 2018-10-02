from __future__ import unicode_literals

from numpy.testing import assert_almost_equal

from ncephes import ellie, ellik, ellpe, ellpk


def test_ellie():
    assert_almost_equal(ellie(-5.3, 0.12), -5.12290521194)


def test_ellik():
    assert_almost_equal(ellik(-5.3, 0.12), -5.48607395126)


def test_ellpe():
    assert_almost_equal(ellpe(0.4), 1.3993921388974322)


def test_ellpk():
    assert_almost_equal(ellpk(0.4), 1.7775193714912534)
