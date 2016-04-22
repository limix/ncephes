from __future__ import absolute_import
import glob
from os.path import join
from cffi import FFI
import pycparser

class FuncSign(object):
    def __init__(self, name, ret_type):
        self.name = name
        self.ret_type = ret_type
        self.param_names = []
        self.param_types = []

    def __str__(self):
        n = len(self.param_names)
        pnames = self.param_names
        ptypes = self.param_types

        sparams = ('%s %s' % (ptypes[i], pnames[i]) for i in range(n))
        sparams = str(tuple(sparams))
        sparams = sparams.replace("'", "")
        s = '%s %s%s' % (self.ret_type, self.name, sparams)
        s = s.replace(',)', ')')
        return s

class FuncDefVisitor(pycparser.c_ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def _parse_param_signature(self, p):
        name = getattr(p.type, 'declname', '')

        suffix = ''
        t = p.type.type
        while not hasattr(t, 'names'):
            t = t.type
            suffix += '*'
        typ = t.names[0]
        return (name, typ+suffix)

    def visit_FuncDef(self, node):
        ret_type = node.decl.type.type.type.names[0]
        if len(node.decl.storage) == 0:
            fs = FuncSign(node.decl.name, ret_type)
            for p in node.param_decls:
                (name, typ) = self._parse_param_signature(p)
                fs.param_names.append(name)
                fs.param_types.append(typ)
            self.functions.append(fs)

def fetch_func_decl(filename):
    parser = pycparser.CParser()
    text = pycparser.preprocess_file(filename, 'cpp', '')
    text_clean = text.replace('\x0c', '')
    ast = parser.parse(text_clean, filename)

    v = FuncDefVisitor()
    v.visit(ast)

    return [str(f) for f in v.functions]

include_dirs = [join('ncephes', 'cephes', 'cprob')]
src_files = glob.glob(join('ncephes', 'cephes', 'cprob', '*.c'))
src_files.append(join('ncephes', 'cephes', 'cmath', 'isnan.c'))

ffi = FFI()

fs = []
for fp in glob.glob(join('ncephes', 'cephes', 'cprob', '*.c')):
    if not fp.endswith('mtherr.c'):
        fs.extend(fetch_func_decl(fp))

ffi.set_source('ncephes._cprob_ffi',
        ';\n'.join(['extern ' + s for s in fs])+';',
        include_dirs=include_dirs,
        sources=src_files,
        libraries=[])
ffi.cdef(';'.join(fs)+';')

if __name__ == '__main__':
    ffi.compile(verbose=True)
