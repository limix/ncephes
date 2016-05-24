Cumulative distribution function
================================

.. py:function:: fdtr(df1, df2, x)

    Returns the area from zero to x under the F density
    function (also known as Snedcor's density or the
    variance ratio density).

    :param int df1: degrees of freedom
    :param int df2: degrees of freedom
    :param float x: positive F variable

Description
-----------

This is the density of x = (u1/df1)/(u2/df2), where u1 and u2 are random
variables having Chi square distributions with df1
and df2 degrees of freedom, respectively.

The incomplete beta integral is used according to the formula::

    P(x) = incbet(df1/2, df2/2, (df1 * x/(df2 + df1*x))

The arguments a and b are greater than zero, and x is
nonnegative.

Accuracy
--------

Tested at random points (a, b, x).

+----------+------+--------+--------+---------------+
|          |x     |a, b    |        |relative error |
+----------+------+--------+--------+-------+-------+
|arithmetic|domain|domain  |# trials|peak   |rms    |
+==========+======+========+========+=======+=======+
|IEEE      |0, 1  |0, 100  |100000  |9.8e-15|1.7e-15|
+----------+------+--------+--------+-------+-------+
|IEEE      |1, 5  |0, 100  |100000  |6.5e-15|3.5e-16|
+----------+------+--------+--------+-------+-------+
|IEEE      |0, 1  |1, 10000|100000  |2.2e-11|3.3e-12|
+----------+------+--------+--------+-------+-------+
|IEEE      |1, 5  |1, 10000|100000  |1.1e-11|1.7e-13|
+----------+------+--------+--------+-------+-------+

See also :py:func:`incbet`.

Error messages
--------------

+-----------+-------------+--------------+
|message    |condition    |value returned|
+===========+=============+==============+
|fdtr domain|a<0, b<0, x<0|0             |
+-----------+-------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#fdtr
