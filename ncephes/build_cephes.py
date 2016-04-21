import glob
import os
from os.path import join

from cffi import FFI

curdir = os.path.abspath(os.path.dirname(__file__))

cephes_root = join(curdir, 'cephes')

include_dirs = [cephes_root]

cephes_src = glob.glob(join(cephes_root, 'cprob/*.c'))
cephes_hdr = glob.glob(join(cephes_root, 'cprob/*.h'))

# cephes_src = glob.glob(join(cephes_root, '*/*.c'))
#
# cephes_hdr = glob.glob(join(cephes_root, '*/*.h'))

ffi = FFI()
ffi.set_source('_cephes_ffi', "double incbet(double, double, double);",
        include_dirs=include_dirs,
        sources=cephes_src,
        libraries=[])

if __name__ == '__main__':
    ffi.compile(verbose=True)
