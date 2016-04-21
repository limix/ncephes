from ncephes import cprob
from numba import jit
import unittest

@jit
def incbet(a, b, x):
    return cprob.incbet(a, b, x)

@jit
def erf(x):
    return cprob.erf(x)

class TestNumba(unittest.TestCase):
    def test_incbet(self):
        self.assertAlmostEqual(incbet(1., 3., 0.3), 0.657)

    def test_erf(self):
        self.assertAlmostEqual(cprob.erf(1.3), 0.9340079449406524)

if __name__ == '__main__':
    unittest.main()
