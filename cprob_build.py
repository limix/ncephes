# TODO: Add support for the files cprob/drand.c and cprob/polevl.c.
from cffi import FFI

from build_helpers import get_info


def make():
    d = get_info('cprob')

    fdecl_extern = ';\n'.join(['extern ' + f for f in d['fdecls']]) + ';'
    fdecl_noextern = ';'.join(d['fdecls']) + ';'

    ffi = FFI()
    ffi.set_source('ncephes._cprob_ffi',
                   fdecl_extern,
                   include_dirs=d['include_dirs'],
                   sources=d['src_files'],
                   libraries=[])
    ffi.cdef(fdecl_noextern)
    return ffi
