Binomial distribution
=====================
.. py:function:: bdtr(k, n, p)

    Returns the sum of the terms 0 through k of the Binomial
    probability density. The function is defined as:

    :param int k: number of successes within [0, n]
    :param int n: number of trials
    :param float p: probability of success within [0, 1]

See also :py:func:`bdtrc` and :py:func:`bdtri`.

Description
-----------

.. math::
    \sum_{j=0}^k {n \choose j} p^j (1-p)^{n-j}

The terms are not summed directly; instead the incomplete
beta integral is employed, according to the formula::

    y = bdtr(k, n, p) = incbet(n - k, k +1, 1 - p)

The arguments must be positive, with p ranging from 0 to 1.

Accuracy
--------

Tested at random points (a, b, p), with p between 0 and 1.

+----------+------+--------+---------------+
|          | a, b |        |relative error |
+----------+------+--------+-------+-------+
|arithmetic|domain|# trials|peak   |rms    |
+==========+======+========+=======+=======+
|For p between 0.001 and 1                 |
+----------+------+--------+-------+-------+
|IEEE      |0, 100|100000  |4.3e-15|2.6e-16|
+----------+------+--------+-------+-------+

See also :py:func:`incbi`.

Error messages
--------------

+-----------+------------+--------------+
|message    |condition   |value returned|
+===========+============+==============+
|bdtr domain|k < 0       |0.0           |
+           +------------+              +
|           |n < k       |              |
+           +------------+              +
|           |x < 0, x > 1|              |
+-----------+------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#bdtr
