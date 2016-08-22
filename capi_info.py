from os.path import join

import module_info


def get_capi_module_name(module):
    return 'ncephes.lib.' + 'n' + module


def get_sources(module):
    sources = module_info.get_sources(module)
    sources += [join('ncephes', 'cephes', module + '_ffcall.c')]
    sources += [join('ncephes', 'cephes', 'const.c')]
    return sources


def get_include_dirs(module):
    from module_info import get_include_dirs as gid
    return gid(module) + [join('ncephes', 'include')]


def get_header(module):
    return join('ncephes', 'include', 'ncephes', module + '.h')
