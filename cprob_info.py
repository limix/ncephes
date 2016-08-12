import re
import glob
from os.path import splitext
from os.path import basename
from os.path import join
from build_helpers import fetch_func_decl
from build_helpers import read_export_file
from build_helpers import forward_call
from build_helpers import api_decl

def get_info():
    include_dirs = [join('ncephes', 'cephes', 'cprob')]
    src_files = glob.glob(join('ncephes', 'cephes', 'cprob', '*.c'))
    src_files.append(join('ncephes', 'cephes', 'cmath', 'isnan.c'))
    export_table = read_export_file(join('ncephes', 'cephes', 'cprob_export.txt'))

    regex = re.compile(r'^.* (.+)\(.*\).*$')
    fdecls = []
    ffcalls = []
    apidecls = []
    for fp in glob.glob(join('ncephes', 'cephes', 'cprob', '*.c')):
        modname = splitext(basename(fp))[0]
        if modname in export_table:
            fnames = export_table[modname]
            fs = []
            for fd in fetch_func_decl(fp):
                fdname = regex.match(fd).group(1)
                for fn in fnames:
                    if fn == fdname:
                        fs.append(fd)
                        ffcalls.append(forward_call(fd))
                        apidecls.append(api_decl(fd))
            fdecls.extend(fs)

    return dict(include_dirs=include_dirs, src_files=src_files, fdecls=fdecls,
                ffcalls=ffcalls, apidecls=apidecls)
