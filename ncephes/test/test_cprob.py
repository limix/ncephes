from ncephes import cprob
import unittest

class TestCprob(unittest.TestCase):
    def test_incbet(self):
        self.assertAlmostEqual(cprob.incbet(1., 3., 0.3), 0.657)

    def test_erf(self):
        self.assertAlmostEqual(cprob.erf(1.3), 0.9340079449406524)

if __name__ == '__main__':
    unittest.main()
