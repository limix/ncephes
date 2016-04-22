from __future__ import absolute_import
from . import _cprob_ffi
from ._cprob_ffi.lib import *
from numba import cffi_support
cffi_support.register_module(_cprob_ffi)
