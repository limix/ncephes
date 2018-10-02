from __future__ import unicode_literals

from ncephes import ffi
from numpy.testing import assert_almost_equal


from ncephes import airy, hyp2f1


def test_airy():
    ai = ffi.new("double *")
    aip = ffi.new("double *")
    bi = ffi.new("double *")
    bip = ffi.new("double *")
    airy(0.2, ai, aip, bi, bip)
    assert_almost_equal(
        [ai[0], aip[0], bi[0], bip[0]],
        [
            0.30370315428638206,
            -0.25240547028561955,
            0.7054642029186613,
            0.46178928436215094,
        ],
    )


def test_hyp2f1():
    assert_almost_equal(hyp2f1(0.2, 1.1, 0.3, -1), 0.6248283119898905)
