from distutils.core import setup, Extension
import ncephes
from os.path import join

module1 = Extension('pkg_name',
                    sources=[join('pkg_name', 'demo.c')],
                    libraries=['ncprob', 'm'],
                    library_dirs=[ncephes.get_lib()],
                    include_dirs=[ncephes.get_include()])

setup(name='PackageName',
      version='1.0',
      description='This is a demo package',
      ext_modules=[module1])
