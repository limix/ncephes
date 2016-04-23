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
        node.decl.type.args.params[0]
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
    ast = pycparser.parse_file(filename, use_cpp=True, cpp_path='cpp',
                               cpp_args='')

    v = FuncDefVisitor()
    v.visit(ast)

    return [str(f) for f in v.functions]
