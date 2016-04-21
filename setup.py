import os
import sys
from setuptools import setup
from setuptools import find_packages

PKG_NAME = 'ncephes'
VERSION  = '0.0.1'

def get_test_suite():
    from unittest import TestLoader
    return TestLoader().discover(PKG_NAME)

def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    metadata = dict(
        name=PKG_NAME,
        version=VERSION,
        maintainer="Limix Developers",
        maintainer_email = "horta@ebi.ac.uk",
        license="BSD",
        url='http://pmbio.github.io/limix/',
        test_suite='setup.get_test_suite',
        packages=find_packages(),
        zip_safe=True,
        setup_requires=["cffi>=1.0.0"],
        cffi_modules=["ncephes/cprob_build.py:ffi"],
        install_requires=["cffi>=1.0.0"],
    )

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)

if __name__ == '__main__':
    setup_package()
