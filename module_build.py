from cffi import FFI

from build_helpers import get_module_info


def _make(module):
    d = get_module_info(module)

    fdecl_extern = ';\n'.join(['extern ' + f for f in d['fdecls']]) + ';'
    fdecl_noextern = ';'.join(d['fdecls']) + ';'

    ffi = FFI()
    ffi.set_source('ncephes._%s_ffi' % module,
                   fdecl_extern,
                   include_dirs=d['include_dirs'],
                   sources=d['src_files'],
                   libraries=[])
    ffi.cdef(fdecl_noextern)
    return ffi

cprob = _make('cprob')
ellf = _make('ellf')
