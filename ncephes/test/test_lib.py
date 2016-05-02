import os
import unittest
from ncephes import get_include

class TestLib(unittest.TestCase):
    def test_get_include(self):
        suffix = os.path.join("ncephes", "cephes", "include")
        self.assertTrue(get_include().endswith(suffix))

if __name__ == '__main__':
    print(get_include())
