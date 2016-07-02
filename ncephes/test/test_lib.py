import os

from numpy.testing import assert_equal

from .. import get_include

def test_get_include():
    suffix = os.path.join("ncephes", "cephes", "include")
    assert_equal(get_include().endswith(suffix), True)
