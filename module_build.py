from os.path import join

from cffi import FFI

from module_info import get_fdecls
from module_info import get_include_dirs
from module_info import get_sources


def _make(module):
    fdecls = get_fdecls(module)

    fdecl_extern = '\n'.join(['extern ' + f for f in fdecls])
    fdecl_noextern = '\n'.join(fdecls)

    cconst = join('ncephes', 'cephes', 'const.c')

    ffi = FFI()
    ffi.set_source('ncephes._%s_ffi' % module,
                   fdecl_extern,
                   include_dirs=get_include_dirs(module),
                   sources=get_sources(module) + [cconst],
                   libraries=[],
                   language='c')
    ffi.cdef(fdecl_noextern)
    return ffi

cprob = _make('cprob')
ellf = _make('ellf')
misc = _make('misc')
polyn = _make('polyn')
