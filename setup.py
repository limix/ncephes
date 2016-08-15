import os
from setuptools import setup
from setuptools.command.build_ext import build_ext
from os.path import join
import sys
from setuptools import find_packages

from pycparser import parse_file

from build_helpers import get_supported_modules
from build_capi import build_capi
from capi_info import get_header

pkg_name = 'ncephes'
version = '0.0.8.dev4'


class _build_ext(build_ext):

    def run(self):
        self.reinitialize_command('build_capi', inplace=1)
        self.run_command("build_capi")
        return build_ext.run(self)


def _check_pycparser():
    try:
        parse_file(join('ncephes', 'cephes', 'cmath', 'isnan.c'),
                   use_cpp=True, cpp_path='cpp', cpp_args='')
    except RuntimeError:
        print('Error: could not parse a C file. Do you have a working C/C++' +
              ' compiler system?')
        sys.exit(1)


def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)
    _check_pycparser()

    with open('requirements.txt') as f:
        requires = [row.strip() for row in f.readlines()]

    setup_requires = requires + ['pytest-runner']
    tests_require = ['pytest']

    long_description = ("Python interface for the Cephes library. " +
                        "It also supports Numba and its nopython mode.")

    modules = get_supported_modules()
    cffi_modules = ['module_build.py:%s' % m for m in modules]

    data_files = []
    data_files += [(join('ncephes', 'include', 'ncephes'),
                    [get_header(m) for m in modules])]

    metadata = dict(
        name=pkg_name,
        version=version,
        maintainer="Danilo Horta",
        maintainer_email="danilo.horta@gmail.com",
        author="Danilo Horta",
        author_email="danilo.horta@gmail.com",
        description="Python interface for the Cephes library.",
        long_description=long_description,
        license="BSD",
        url='https://github.com/Horta/ncephes',
        packages=find_packages(),
        zip_safe=False,
        setup_requires=setup_requires,
        cffi_modules=cffi_modules,
        install_requires=requires,
        tests_require=tests_require,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Topic :: Scientific/Engineering"
        ],
        cmdclass={'build_capi': build_capi, 'build_ext': _build_ext},
        keywords=["cephes", "math", "numba"],
        data_files=[(join('ncephes', 'include', 'ncephes'),
                     [get_header(module) for module in modules])],
    )

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)

if __name__ == '__main__':
    try:
        __import__("numpy")
    except ImportError:
        msg = "Error: numpy package couldn't be found."
        msg += " Please, install it first so I can proceed."
        print(msg)
        sys.exit(1)

    setup_package()
