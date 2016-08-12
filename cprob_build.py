# TODO: Add support for the files cprob/drand.c and cprob/polevl.c.
from cffi import FFI

from cprob_info import get_info


d = get_info()

fdecl_extern = ';\n'.join(['extern ' + f for f in d['fdecls']]) + ';'
fdecl_noextern = ';'.join(d['fdecls']) + ';'

ffi = FFI()
ffi.set_source('ncephes._cprob_ffi',
               fdecl_extern,
               include_dirs=d['include_dirs'],
               sources=d['src_files'],
               libraries=[])
ffi.cdef(fdecl_noextern)
# ffi.embedding_api("extern double ncephes_bdtrc(int k, int n, double p);")
# import ipdb; ipdb.set_trace()
# ffi.embedding_api(ffcalls)
# ffi.compile(target="cprob-0.1.*", verbose=True)
