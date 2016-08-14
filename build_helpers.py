from os.path import splitext
from os.path import basename
from os.path import join

from glob import glob

import re

from pycparser import parse_file
from pycparser.c_parser import CParser
from pycparser.c_ast import NodeVisitor


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
    ast = parse_file(filename, use_cpp=True, cpp_path='cpp', cpp_args='')

    v = FuncDefVisitor()
    v.visit(ast)

    return [str(f) for f in v.functions]


def _rcs(s):
    if s.startswith('cephes_'):
        return s[len('cephes_'):]
    return s


def api_decl(decl):
    parser = CParser()
    decl = parser.parse(decl + ';', filename='<stdin>').ext[0]
    name = decl.name
    args = decl.type.args
    nargs = len(args.params)
    if len(decl.type.type.type.names) > 1:
        import ipdb
        ipdb.set_trace()
    else:
        rtype = decl.type.type.type.names[0]
    ndecl = rtype + ' ncephes_' + _rcs(name) + '('
    for param in args.params:
        if len(param.type.type.names) > 1:
            import ipdb
            ipdb.set_trace()
        typ = param.type.type.names[0]
        ndecl += typ + ' ' + param.name + ', '
    if nargs > 0:
        ndecl = ndecl[:-2]
    return ndecl + ');'


def forward_call(decl):
    parser = CParser()
    decl = parser.parse(decl + ';', filename='<stdin>').ext[0]
    name = decl.name
    args = decl.type.args
    nargs = len(args.params)
    if len(decl.type.type.type.names) > 1:
        import ipdb
        ipdb.set_trace()
    else:
        rtype = decl.type.type.type.names[0]
    ndecl = rtype + ' ncephes_' + _rcs(name) + '('
    call_expr = name + '('
    for param in args.params:
        if len(param.type.type.names) > 1:
            import ipdb
            ipdb.set_trace()
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


def get_module_info(module):
    include_dirs = [join('ncephes', 'cephes', module)]
    src_files = glob(join('ncephes', 'cephes', module, '*.c'))
    src_files.append(join('ncephes', 'cephes', 'cmath', 'isnan.c'))
    export_table = read_export_file(join('ncephes', 'cephes',
                                         '%s_export.txt' % module))

    regex = re.compile(r'^.* (.+)\(.*\).*$')
    fdecls = []
    ffcalls = []
    apidecls = []
    for fp in glob(join('ncephes', 'cephes', module, '*.c')):
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


def get_libs_info():

    if get_libs_info.return_ is None:

        supms = open('supported_modules.txt').read().split("\n")[:-1]
        incl = join('ncephes', 'include')
        lib = join('ncephes', 'lib')
        libraries = []
        hdr_files = []
        lib_files = []

        for supm in [s for s in supms if s == 'cprob']:
            srcs = get_module_info(supm)['src_files']
            srcs.append(join('ncephes', 'cephes', supm + '_ffcall.c'))
            v = ('n' + supm, {'sources': srcs, 'include_dirs': [incl]})
            libraries.append(v)
            hdr_files.append(join(incl, 'ncephes', supm + '.h'))
            lib_files.append(join(lib, 'libn' + supm + '.a'))

        cffi_modules = []
        for supm in supms:
            cffi_modules.append("module_build.py:" + supm)

        data_files = [(join(incl, 'ncephes'), hdr_files), (lib, lib_files)]
        get_libs_info.return_ = dict(libraries=libraries,
                                     data_files=data_files,
                                     cffi_modules=cffi_modules)

    return get_libs_info.return_
get_libs_info.return_ = None
