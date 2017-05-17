from __future__ import unicode_literals

import sys
PY3 = sys.version_info > (3,)

from os.path import join

from cffi import FFI

from module_info import get_fdecls
from module_info import get_include_dirs
from module_info import get_sources
from build_helpers import backward_call


def _make(module):

    fdecls = get_fdecls(module)

    fdecls_intern = []
    backward = []
    for fd in fdecls:
        if module == 'cprob':
            if any([(i in fd) for i in ['ncephes_cosm1', 'ncephes_expm1', 'ncephes_log1p']]):
                backward.append(backward_call(fd))
        fd = fd.replace('ncephes_', '')
        fdecls_intern.append(fd)

    fdecl_extern = '\n'.join(['extern ' + f for f in fdecls])
    fdecl_intern = '\n'.join(fdecls_intern)
    cconst = join('ncephes', 'cephes', 'const.c')
    sources = get_sources(module) + [cconst]

    if module == 'misc':
        sources += [join('ncephes', 'cephes', 'cprob', 'unity.c')]

    if not PY3:
        fdecl_extern = fdecl_extern.encode('ascii', 'ignore')
        fdecl_intern = fdecl_intern.encode('ascii', 'ignore')
        sources = [s.encode('ascii', 'ignore') for s in sources]

    ffi = FFI()
    ffi.set_source('ncephes._%s_ffi' % module,
                   fdecl_extern + '\n' + '\n'.join(backward),
                   include_dirs=get_include_dirs(module),
                   sources=sources,
                   libraries=[],
                   extra_compile_args=['-Ofast'],
                   language='c')
    ffi.cdef(fdecl_intern)
    return ffi

cprob = _make('cprob')
ellf = _make('ellf')
misc = _make('misc')
polyn = _make('polyn')
