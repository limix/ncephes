Inverse of the cumulative distribution function
===============================================
.. py:function:: bdtri(k, n, y)

    Finds the event probability p such that the sum of the
    terms 0 through k of the Binomial probability density
    is equal to the given cumulative probability y.

    :param int k: number of successes within [0, n]
    :param int n: number of trials
    :param float y: cumulative probability within [0, 1]

See also :py:func:`bdtr` and :py:func:`bdtrc`.

Description
-----------

This is accomplished using the inverse beta integral
function and the relation::

    1 - p = incbi(n - k, k + 1, y)

Accuracy
--------

Tested at random points (a, b, p).

+----------+--------+--------+---------------+
|          |a, b    |        |relative error |
+----------+--------+--------+-------+-------+
|arithmetic|domain  |# trials|peak   |rms    |
+==========+========+========+=======+=======+
|For p between 0.001 and 1                   |
+----------+--------+--------+-------+-------+
|IEEE      |0, 100  |100000  |2.3e-14|6.4e-16|
+----------+--------+--------+-------+-------+
|IEEE      |0, 10000|100000  |6.6e-12|1.2e-13|
+----------+--------+--------+-------+-------+
|For p between 10^-6 and 0.001               |
+----------+--------+--------+-------+-------+
|IEEE      |0, 100  |100000  |2.0e-12|1.3e-14|
+----------+--------+--------+-------+-------+
|IEEE      |0, 10000|100000  |1.5e-12|3.2e-14|
+----------+--------+--------+-------+-------+

See also :py:func:`incbi`.

Error messages
--------------

+------------+-------------+--------------+
|message     |condition    |value returned|
+============+=============+==============+
|bdtri domain|k < 0, n <= k|0.0           |
+            +-------------+              +
|            |x < 0, x > 1 |              |
+------------+-------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#bdtri
