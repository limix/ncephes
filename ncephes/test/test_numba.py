from __future__ import unicode_literals

from ncephes import cprob
from ncephes.cprob import incbet
from numpy.testing import assert_almost_equal

try:
    from numba import jit

    @jit(nogil=True, nopython=True)
    def _incbet(a, b, x):
        return incbet(a, b, x)

    @jit(nogil=True)
    def erf(x):
        return cprob.erf(x)

    def test_incbet():
        assert_almost_equal(_incbet(1., 3., 0.3), 0.657)

    def test_erf():
        assert_almost_equal(erf(1.3), 0.9340079449406524)

except ImportError:
    pass
