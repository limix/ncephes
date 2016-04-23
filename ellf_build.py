import re
import glob
from os.path import splitext
from os.path import basename
from os.path import join
from cffi import FFI
import pycparser
from build_helpers import fetch_func_decl
from build_helpers import read_export_file

include_dirs = [join('ncephes', 'cephes', 'ellf')]
src_files = glob.glob(join('ncephes', 'cephes', 'ellf', '*.c'))
src_files.append(join('ncephes', 'cephes', 'cmath', 'isnan.c'))
export_table = read_export_file(join('ncephes', 'cephes', 'ellf_export.txt'))

ffi = FFI()

regex = re.compile(r'^.* (.+)\(.*\).*$')
fs = []
for fp in glob.glob(join('ncephes', 'cephes', 'ellf', '*.c')):
    modname = splitext(basename(fp))[0]
    if modname in export_table:
        fnames = export_table[modname]
        fdecls = []
        for fd in fetch_func_decl(fp):
            fdname = regex.match(fd).group(1)
            for fn in fnames:
                if fn == fdname:
                    fdecls.append(fd)
        fs.extend(fdecls)

ffi.set_source('ncephes._ellf_ffi',
        ';\n'.join(['extern ' + s for s in fs])+';',
        include_dirs=include_dirs,
        sources=src_files,
        libraries=[])
ffi.cdef(';'.join(fs)+';')

if __name__ == '__main__':
    ffi.compile(verbose=True)
