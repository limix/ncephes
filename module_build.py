from __future__ import unicode_literals

import sys
PY3 = sys.version_info > (3,)

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
    sources = get_sources(module) + [cconst]

    if not PY3:
        fdecl_extern = fdecl_extern.encode('ascii', 'ignore')
        fdecl_noextern = fdecl_noextern.encode('ascii', 'ignore')
        sources = [s.encode('ascii', 'ignore') for s in sources]

    ffi = FFI()
    ffi.set_source('ncephes._%s_ffi' % module,
                   fdecl_extern,
                   include_dirs=get_include_dirs(module),
                   sources=sources,
                   libraries=[],
                   extra_compile_args=['-Ofast'],
                   language='c')
    ffi.cdef(fdecl_noextern)
    return ffi

cprob = _make('cprob')
ellf = _make('ellf')
misc = _make('misc')
polyn = _make('polyn')
