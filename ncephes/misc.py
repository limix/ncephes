from __future__ import unicode_literals

from . import _misc_ffi
from ._misc_ffi.lib import *

try:
    from numba import cffi_support as _cffi_support
    _cffi_support.register_module(_misc_ffi)
except ImportError:
    pass
