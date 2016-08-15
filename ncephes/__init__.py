from __future__ import absolute_import

import pkg_resources
try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    __version__ = 'unknown'

from .api import get_include
from .api import get_lib
from . import cprob
from . import ellf


def test():
    import os

    p = __import__('ncephes').__path__[0]
    src_path = os.path.dirname(os.path.abspath(p))
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        return_code = __import__('pytest').main()
    finally:
        os.chdir(old_path)

    return return_code
