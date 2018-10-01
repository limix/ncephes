from __future__ import unicode_literals

from numpy.testing import assert_almost_equal

from ncephes import lbeta


def test_lbeta():
    assert_almost_equal(lbeta(10, 3), -6.4922398350204711)
