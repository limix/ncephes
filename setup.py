import os
from setuptools import setup

if __name__ == "__main__":

    on_rtd = os.environ.get("READTHEDOCS") == "True"
    if on_rtd:
        setup()
    else:
        setup(cffi_modules="build_ext.py:ffibuilder")
