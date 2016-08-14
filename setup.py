import os
from setuptools import setup
from setuptools.command.build_ext import build_ext
from os.path import join
import sys
from setuptools import find_packages

from pycparser import parse_file

from build_helpers import get_libs_info
from build_capi import build_capi

pkg_name = 'ncephes'
version = '0.0.8.dev4'


class BuildExt(build_ext):

    def run(self):
        import ipdb
        ipdb.set_trace()
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

    dlib = get_libs_info()

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
        cffi_modules=dlib['cffi_modules'],
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
        cmdclass={'build_capi': build_capi, 'build_ext': BuildExt},
        keywords=["cephes", "math", "numba"],
        data_files=dlib['data_files'],
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
