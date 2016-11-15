from __future__ import unicode_literals

from pycparser import parse_file
from pycparser.c_parser import CParser
from pycparser.c_ast import NodeVisitor

def get_supported_modules():
    return open('supported_modules.txt').read().split("\n")[:-1]

def _check_executable(executable):
    from distutils.spawn import find_executable
    return not(find_executable(executable) is None)

def _cpp_executable():
    if _check_executable('cpp'):
        return 'cpp'
    elif _check_executable('cl'):
        return 'cl'
    elif _check_executable('gcc'):
        return 'gcc'
    elif _check_executable('clang'):
        return 'clang'
    return 'cpp'

def _cpp_args():
    args = ['-Incephes/cephes']
    if _cpp_executable() == 'cl':
        args += ['/nologo', '/EP']
    return args

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

        sparams = [('%s %s' % (ptypes[i], pnames[i])) for i in range(n)]
        sparams = ', '.join(sparams)
        s = '%s %s(%s)' % (self.ret_type, self.name, sparams)
        return s


class FuncDefVisitor(NodeVisitor):

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
        return (name, typ + suffix)

    def visit_FuncDef(self, node):
        ret_type = node.decl.type.type.type.names[0]
        if len(node.decl.storage) == 0:
            fs = FuncSign(node.decl.name, ret_type)
            for p in node.decl.type.args.params:
                (name, typ) = self._parse_param_signature(p)
                fs.param_names.append(name)
                fs.param_types.append(typ)
            self.functions.append(fs)


def read_export_file(fp):
    lines = open(fp).read().split('\n')
    lines = [l for l in lines if len(l.strip()) > 0]
    d = dict()
    for line in lines:
        modname, funcnames = line.split(':')
        modname = modname.strip()
        d[modname] = [f.strip() for f in funcnames.split(',')]
    return d


def fetch_func_decl(filename):
    cpp_path = _cpp_executable()
    cpp_args = _cpp_args()
    ast = parse_file(filename, use_cpp=True, cpp_path=cpp_path,
                      cpp_args=cpp_args)

    v = FuncDefVisitor()
    v.visit(ast)

    return [str(f) for f in v.functions]


def _rcs(s):
    if s.startswith('cephes_'):
        return s[len('cephes_'):]
    return s


def api_fdecls(decl):
    parser = CParser()
    decl = parser.parse(decl, filename='<stdin>').ext[0]
    name = decl.name
    args = decl.type.args
    nargs = len(args.params)
    if len(decl.type.type.type.names) > 1:
        assert False
    else:
        rtype = decl.type.type.type.names[0]
    ndecl = rtype + ' ncephes_' + _rcs(name) + '('
    for param in args.params:
        if len(param.type.type.names) > 1:
            assert False
        typ = param.type.type.names[0]
        ndecl += typ + ' ' + param.name + ', '
    if nargs > 0:
        ndecl = ndecl[:-2]
    return ndecl + ');'


def forward_call(decl):
    parser = CParser()
    decl = parser.parse(decl, filename='<stdin>').ext[0]
    name = decl.name
    args = decl.type.args
    nargs = len(args.params)
    if len(decl.type.type.type.names) > 1:
        assert False
    else:
        rtype = decl.type.type.type.names[0]
    ndecl = rtype + ' ncephes_' + _rcs(name) + '('
    call_expr = name + '('
    for param in args.params:
        if len(param.type.type.names) > 1:
            assert False
        typ = param.type.type.names[0]
        ndecl += typ + ' ' + param.name + ', '
        call_expr += param.name + ', '
    if nargs > 0:
        ndecl = ndecl[:-2]
        call_expr = call_expr[:-2]
    ndecl += ')'
    call_expr += ')'
    ndecl += " { return %s; }" % call_expr
    return ndecl
