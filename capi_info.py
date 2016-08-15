from os.path import join

import module_info


def get_capi_module_name(module):
    return 'n' + module


def get_sources(module):
    sources = module_info.get_sources(module)
    sources += [join('ncephes', 'cephes', module + '_ffcall.c')]
    return sources


def get_include_dirs(module):
    from module_info import get_include_dirs as gid
    return gid(module) + [join('ncephes', 'include')]


def get_header(module):
    return join('ncephes', 'include', 'ncephes', module + '.h')
    # def get_module_info(module):
    #     include_dirs = [join('ncephes', 'cephes', module)]
    #     src_files = glob(join('ncephes', 'cephes', module, '*.c'))
    #     src_files.append(join('ncephes', 'cephes', 'cmath', 'isnan.c'))
    #     export_table = read_export_file(join('ncephes', 'cephes',
    #                                          '%s_export.txt' % module))
    #
    #     regex = re.compile(r'^.* (.+)\(.*\).*$')
    #     fdecls = []
    #     ffcalls = []
    #     apidecls = []
    #     for fp in glob(join('ncephes', 'cephes', module, '*.c')):
    #         modname = splitext(basename(fp))[0]
    #         if modname in export_table:
    #             fnames = export_table[modname]
    #             fs = []
    #             for fd in fetch_func_decl(fp):
    #                 fdname = regex.match(fd).group(1)
    #                 for fn in fnames:
    #                     if fn == fdname:
    #                         fs.append(fd)
    #                         ffcalls.append(forward_call(fd))
    #                         apidecls.append(api_decl(fd))
    #             fdecls.extend(fs)
    #
    #     return dict(include_dirs=include_dirs, src_files=src_files, fdecls=fdecls,
    #                 ffcalls=ffcalls, apidecls=apidecls)
