from os.path import splitext
from os.path import basename
from os.path import join
from build_helpers import read_export_file
from build_helpers import fetch_func_decl

from glob import glob

import re


def get_sources(module):
    sources = glob(join('ncephes', 'cephes', module, '*.c'))
    sources += [join('ncephes', 'cephes', 'cmath', 'isnan.c')]
    return sources


def get_include_dirs(module):
    return [join('ncephes', 'cephes', module)]


def get_fdecls(module):
    regex = re.compile(r'^.* (.+)\(.*\).*$')
    fdecls = []
    export_table = read_export_file(join('ncephes', 'cephes',
                                         '%s_export.txt' % module))
    for fp in glob(join('ncephes', 'cephes', module, '*.c')):
        modname = splitext(basename(fp))[0]
        if modname in export_table:
            fnames = export_table[modname]
            for fd in fetch_func_decl(fp):
                fdname = regex.match(fd).group(1)
                for fn in fnames:
                    if fn == fdname:
                        fdecls.append(fd + ';')

    return fdecls


def get_extra_compile_args():
    return []
