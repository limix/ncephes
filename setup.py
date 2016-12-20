from __future__ import unicode_literals

import os
from os.path import join
import sys
PY3 = sys.version_info > (3,)
from setuptools import setup
from setuptools import find_packages

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(OSError, IOError, ImportError):
    long_description = open('README.md').read()

def get_sources(module):
    from module_info import get_sources
    sources = get_sources(module)
    sources += [join('ncephes', 'cephes', module + '_ffcall.c')]
    sources += [join('ncephes', 'cephes', 'const.c')]
    return sources


def get_include_dirs(module):
    from module_info import get_include_dirs as gid
    return (gid(module) + [join('ncephes', 'include')] +
            [join('ncephes', 'cephes')])


class GetApi(object):

    def __init__(self, module):
        self._module = module

    def __call__(self):
        from build_capi import CApiLib
        module = self._module
        return CApiLib(name='ncephes.lib.' + 'n' + module,
                       sources=get_sources(module),
                       include_dirs=get_include_dirs(module))


def create_capi_libs():
    modules = open('supported_modules.txt').read().split("\n")[:-1]
    return [GetApi(module) for module in modules]


def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
    pytest_runner = ['pytest-runner'] if needs_pytest else []

    setup_requires = ['build-capi', 'cffi>=1.7',
                      'pycparser'] + pytest_runner
    install_requires = ['cffi>=1.7']
    tests_require = ['numpy']
    recommended = {"numba": ["numba>=0.28"]}

    modules = open('supported_modules.txt').read().split("\n")[:-1]
    cffi_modules = ['module_build.py:%s' % m for m in modules]

    hdr_dir = join('ncephes', 'include', 'ncephes')
    hdr_files = [join(hdr_dir, m + '.h') for m in modules]

    if PY3:
        package_data={'': [join('ncephes', 'lib', '*.*')]}
    else:
        package_data={b'': [join(b'ncephes', b'lib', b'*.*')]}

    metadata = dict(
        name='ncephes',
        version='1.0.16',
        maintainer="Danilo Horta",
        maintainer_email="danilo.horta@gmail.com",
        description="Python interface for the Cephes library.",
        long_description=long_description,
        license="MIT",
        url='https://github.com/glimix/ncephes',
        packages=find_packages(),
        zip_safe=False,
        cffi_modules=cffi_modules,
        setup_requires=setup_requires,
        install_requires=install_requires,
        tests_require=tests_require,
        extras_require=recommended,
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Operating System :: OS Independent",
        ],
        capi_libs=create_capi_libs(),
        keywords=["cephes", "math", "numba"],
        include_package_data=True,
        data_files=[(hdr_dir, hdr_files)],
        package_data=package_data,
    )

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)

if __name__ == '__main__':
    setup_package()
