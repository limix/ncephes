[![Travis branch](https://img.shields.io/travis/Horta/ncephes/master.svg?style=flat-square&label=build)](https://travis-ci.org/Horta/ncephes)  [![PyPI](https://img.shields.io/pypi/v/ncephes.svg?style=flat-square&label=release%20(pypi))](https://pypi.python.org/pypi/ncephes/) [![Documentation Status](https://readthedocs.org/projects/ncephes/badge/?version=latest&style=flat-square)](http://ncephes.readthedocs.org/en/latest/?badge=latest)

nCephes
=======

This package provides a python interface for the
[Cephes library](http://www.netlib.org/cephes/).

Usage
-----

```python
from ncephes import cprob
print(cprob.incbet(1., 3., 0.3))
# prints 0.657
```

You can also call them inside a numba function
```python
from ncephes import cprob
from numba import jit

@jit
def numba_incbet(a, b, x):
    return cprob.incbet(a, b, x)

print(numba_incbet(1., 3., 0.3))
# prints 0.657
```
with nopython mode and nogil enabled
```python
from ncephes import cprob
from numba import jit

incbet = cprob.incbet

@jit(nogil=True, nopython=True)
def numba_incbet(a, b, x):
    return incbet(a, b, x)

print(numba_incbet(1., 3., 0.3))
# prints 0.657
```

One can also statically link the compiled Cephes libraries `ncprob` and
`ncellf`. Please, have a peek at the `examples/prj_name` for a minimalistic
example.

Install
-------

It should be as simple as
```
pip install ncephes
```
Alternatively, you might want to do
```
python setup.py install
```
from the package's root folder.
