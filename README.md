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

Install
-------

It should be as simple as
```
pip install ncehes
```
From source, you might want to do
```
python setup.py install
```
from the package's root folder.
