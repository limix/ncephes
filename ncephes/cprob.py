from __future__ import unicode_literals

from . import _cprob_ffi
from ._cprob_ffi.lib import *
try:
    from numba import cffi_support as _cffi_support
    _cffi_support.register_module(_cprob_ffi)
except ImportError:
    pass
