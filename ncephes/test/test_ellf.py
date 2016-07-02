from .. import ellf
import unittest

class TestEllf(unittest.TestCase):
    def test_ellie(self):
        self.assertAlmostEqual(ellf.ellie(-5.3, 0.12), -5.12290521194)

    def test_ellik(self):
        self.assertAlmostEqual(ellf.ellik(-5.3, 0.12), -5.48607395126)

    def test_ellpe(self):
        self.assertAlmostEqual(ellf.ellpe(0.12), 1.120741662164857)

    def test_ellpk(self):
        self.assertAlmostEqual(ellf.ellpk(0.12), 2.492635323239716)

if __name__ == '__main__':
    unittest.main()
