from __future__ import unicode_literals

from . import _ellf_ffi
from ._ellf_ffi.lib import *

try:
    from numba import cffi_support as _cffi_support
    _cffi_support.register_module(_ellf_ffi)
except ImportError:
    pass
