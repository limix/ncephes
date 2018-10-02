Incomplete beta function
========================
.. py:function:: incbet(a, b, x)

    Returns incomplete beta integral of the arguments, evaluated
    from zero to x. The function is defined as

    :param float a: a positive number
    :param float b: a positive number
    :param float x: any number within [0, 1]

See also :py:func:`incbi`.

Description
-----------

.. math::
    \frac{\Gamma(a+b)}{\Gamma(a)+\Gamma(b)} \int_0^xt^{a-1}(1-t)^{b-1} dt

The domain of definition is 0 <= x <= 1.  In this
implementation a and b are restricted to positive values.
The integral from x to 1 may be obtained by the symmetry
relation::

    1 - incbet(a, b, x)  =  incbet(b, a, 1 - x)

The integral is evaluated by a continued fraction expansion
or, when b*x is small, by a power series.

Accuracy
--------

Tested at uniformly distributed random points (a, b, x) with a and b
in "domain" and x between 0 and 1.

+-----------+-----------+------------+------------+-----------+
|                                    |  Relative error        |
+-----------+-----------+------------+------------+-----------+
|arithmetic |  domain   |  # trials  |    peak    |     rms   |
+===========+===========+============+============+===========+
|   IEEE    |  0,5      |   10000    |   6.9e-15  |   4.5e-16 |
+-----------+-----------+------------+------------+-----------+
|   IEEE    |  0,85     |  250000    |   2.2e-13  |   1.7e-14 |
+-----------+-----------+------------+------------+-----------+
|   IEEE    |  0,1000   |   30000    |   5.3e-12  |   6.3e-13 |
+-----------+-----------+------------+------------+-----------+
|   IEEE    |  0,10000  |  250000    |   9.3e-11  |   7.1e-12 |
+-----------+-----------+------------+------------+-----------+
|   IEEE    |  0,100000 |   10000    |   8.7e-10  |   4.8e-11 |
+-----------+-----------+------------+------------+-----------+

Outputs smaller than the IEEE gradual underflow threshold
were excluded from these statistics.

Error messages
--------------

+----------------+------------+--------------+
|message         |condition   |value returned|
+================+============+==============+
|incbet domain   |x < 0, x > 1|0.0           |
+----------------+            +--------------+
|incbet underflow|            |0.0           |
+----------------+------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#incbet
