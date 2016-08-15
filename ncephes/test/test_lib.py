import os
import six
from os.path import join
from tempfile import mkdtemp
from shutil import rmtree
from subprocess import check_output

from numpy.testing import assert_equal

from ncephes import get_include
from ncephes import get_lib


def test_get_include():
    suffix = os.path.join("ncephes", "include")
    assert_equal(get_include().endswith(suffix), True)


def test_get_lib():
    suffix = os.path.join("ncephes", "lib")
    assert_equal(get_lib().endswith(suffix), True)


def test_link_lib():
    folder = mkdtemp(dir='.')
    testc = join(folder, 'test.c')
    with open(testc, 'w') as f:
        f.write('''
#include <stdio.h>
#include "ncephes/cprob.h"

int main()
{
  printf("incbet: %.3f", ncephes_incbet(1., 3., 0.3));
  return 0;
}
''')
    from distutils.ccompiler import new_compiler
    from distutils import log
    compiler = new_compiler()
    objs = compiler.compile([testc], include_dirs=[get_include()])
    compiler.link_executable(objs, join(folder, 'test_link_lib'),
                             libraries=['ncprob', 'm'],
                             library_dirs=[get_lib()])
    assert_equal(check_output(join(folder, 'test_link_lib'), shell=True),
                 six.b("incbet: 0.657"))
    rmtree(folder)
