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
    cprob.incbet(a, b, x)

print(cprob.incbet(1., 3., 0.3))
# prints 0.657
```
with nopython mode and nogil enabled
```python
from ncephes import cprob
from numba import jit

incbet = cprob.incbet

@jit(nogil=True, nopython=True)
def numba_incbet(a, b, x):
    cprob.incbet(a, b, x)

print(cprob.incbet(1., 3., 0.3))
# prints 0.657
```

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
