import os
import sys
from setuptools import setup
from setuptools import find_packages

pkg_name = 'ncephes'
version = '0.0.7.dev0'

def get_test_suite():
    from unittest import TestLoader
    return TestLoader().discover(pkg_name)

def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)


    requires = ['numba', 'cffi>=1.0.0']

    setup_requires = requires + ['pycparser']
    install_requires = requires

    long_description = ("Python interface for the Cephes library. "+
                        "It also supports Numba and its nopython mode.")

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
        test_suite='setup.get_test_suite',
        packages=find_packages(),
        zip_safe=True,
        setup_requires=setup_requires,
        cffi_modules=["cprob_build.py:ffi", "ellf_build.py:ffi"],
        install_requires=install_requires,
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
        keywords=["cephes", "math", "numba"]
    )

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)

if __name__ == '__main__':
    setup_package()
