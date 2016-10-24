import os
from os.path import join
import sys
from setuptools import setup
from setuptools import find_packages


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

    setup_requires = ['build_capi>=1.0.0', 'cffi>=1.6',
                      'pycparser'] + pytest_runner
    install_requires = ['pytest', 'cffi>=1.6', 'numba>=0.27']
    tests_require = install_requires + ['six']

    long_description = ("Python interface for the Cephes library. " +
                        "It also supports Numba and its nopython mode.")

    modules = open('supported_modules.txt').read().split("\n")[:-1]
    cffi_modules = ['module_build.py:%s' % m for m in modules]

    hdr_dir = join('ncephes', 'include', 'ncephes')
    hdr_files = [join(hdr_dir, m + '.h') for m in modules]

    metadata = dict(
        name='ncephes',
        version='1.0.0',
        maintainer="Danilo Horta",
        maintainer_email="danilo.horta@gmail.com",
        description="Python interface for the Cephes library.",
        long_description=long_description,
        license="MIT",
        url='https://github.com/Horta/ncephes',
        packages=find_packages(),
        zip_safe=False,
        cffi_modules=cffi_modules,
        setup_requires=setup_requires,
        install_requires=install_requires,
        tests_require=tests_require,
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Operating System :: OS Independent",
            "Framework :: Pytest",
        ],
        capi_libs=create_capi_libs(),
        keywords=["cephes", "math", "numba"],
        include_package_data=True,
        data_files=[(hdr_dir, hdr_files)],
        package_data={'': [join('ncephes', 'lib', '*.*')]},
    )

    try:
        from distutils.command.bdist_conda import CondaDistribution
    except ImportError:
        pass
    else:
        metadata['distclass'] = CondaDistribution
        metadata['conda_buildnum'] = 1
        metadata['conda_features'] = ['mkl']

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)

if __name__ == '__main__':
    setup_package()
