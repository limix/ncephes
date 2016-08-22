from numpy.testing import assert_almost_equal

from ncephes import misc


def test_lbeta():
    print(misc.lbeta(10, 3))
    # assert_almost_equal(misc.lbeta(10, 3), -5.12290521194)
