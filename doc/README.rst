NCephes
=======

|Travis| |AppVeyor| |Documentation Status|

This package provides a python interface for the
`Cephes <http://www.netlib.org/cephes/>`__ library. It also supports
`Numba <http://numba.pydata.org>`__ and its ``nopython`` mode.

Usage
-----

.. code:: python

    >>> from ncephes import incbet
    >>> print("{:.3f}".format(incbet(1., 3., 0.3)))
    0.657

You can also call them inside a numba function

.. code:: python

    >>> from ncephes import incbet
    >>> from numba import jit
    >>>
    >>> @jit
    ... def numba_incbet(a, b, x):
    ...     return incbet(a, b, x)
    >>>
    >>> print("{:.3f}".format(numba_incbet(1., 3., 0.3)))
    0.657

and with nopython mode and nogil enabled

.. code:: python

    >>> from ncephes import incbet
    >>> from numba import jit
    >>>
    >>> @jit(nogil=True, nopython=True)
    ... def numba_incbet(a, b, x):
    ...     return incbet(a, b, x)
    >>>
    >>> print("{:.3f}".format(numba_incbet(1., 3., 0.3)))
    0.657

One can also statically link the compiled Cephes libraries ``ncprob``
and ``ncellf``. Please, have a peek at the ``examples/prj_name`` for a
minimalistic example.

Install
-------

The recommended way of installing it is via
`conda <http://conda.pydata.org/docs/index.html>`__

.. code:: bash

    conda install -c conda-forge ncephes

An alternative way would be via pip

.. code:: bash

    pip install ncephes

Running the tests
-----------------

After installation, you can test it

.. code:: bash

    python -c "import ncephes; ncephes.test()"

as long as you have `pytest <http://docs.pytest.org/en/latest/>`__.

Authors
-------

-  **Danilo Horta** -
   `https://github.com/Horta <https://github.com/Horta>`__

License
-------

This project is licensed under the MIT License - see the
`LICENSE <LICENSE>`__ file for details

.. |Travis| image:: https://img.shields.io/travis/limix/ncephes.svg?style=flat-square&label=linux%20%2F%20macos%20build
   :target: https://travis-ci.org/limix/ncephes
.. |AppVeyor| image:: https://img.shields.io/appveyor/ci/Horta/ncephes.svg?style=flat-square&label=windows%20build
   :target: https://ci.appveyor.com/project/Horta/ncephes
.. |Documentation Status| image:: https://readthedocs.org/projects/ncephes/badge/?style=flat-square&version=latest
   :target: https://ncephes.readthedocs.io/
