# TODO: Add support for the files cprob/drand.c and cprob/polevl.c.
from cffi import FFI

from build_helpers import forward_call
from cprob_info import get_info


d = get_info()

fdecl_extern = ';\n'.join(['extern ' + f for f in d['fdecls']]) + ';'
fdecl_noextern = ';'.join(d['fdecls']) + ';'


def make_module():
    ffi = FFI()
    ffi.set_source('ncephes._cprob_ffi',
                   fdecl_extern,
                   include_dirs=d['include_dirs'],
                   sources=d['src_files'],
                   libraries=[])
    ffi.cdef(fdecl_noextern)
    return ffi
#
# def make_api():
#     ffi = FFI()
#     fdecl_cffi_export = '\n'.join(['CFFI_DLLEXPORT ' + forward_call(f)
#                                    for f in d['fdecls']])
#     ffi.set_source('ncephes',
#                    fdecl_extern + '\n' + fdecl_cffi_export,
#                    include_dirs=d['include_dirs'],
#                    sources=d['src_files'],
#                    libraries=[],
#                    extra_link_args=['-install_name @rpath/libcprob.dylib'])
#     ffi.embedding_api('')
#     ffi.compile(target="libcprob.*", verbose=True)
#     return ffi
