from __future__ import absolute_import

from pkg_resources import get_distribution
from pkg_resources import DistributionNotFound

from .api import get_include
from .api import get_lib
from . import cprob
from . import ellf

try:
    __version__ = get_distribution('ncephes').version
except DistributionNotFound:
    __version__ = 'unknown'


def test():
    import os
    p = __import__('ncephes').__path__[0]
    src_path = os.path.abspath(p)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        return_code = __import__('pytest').main(['-q'])
    finally:
        os.chdir(old_path)

    if return_code == 0:
        print("Congratulations. All tests have passed!")

    return return_code
