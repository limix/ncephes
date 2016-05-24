Survival function
=================
.. py:function:: bdtrc(k, n, p)

    Returns the sum of the terms k + 1 through n of the Binomial
    probability density:

    :param int k: number of successes within [0, n]
    :param int n: number of trials
    :param float p: probability of success within [0, 1]

See also :py:func:`bdtr` and :py:func:`bdtri`.

Description
-----------

.. math::
    \sum_{j=k+1}^n {n \choose j} p^j (1-p)^{n-j}


The terms are not summed directly; instead the incomplete
beta integral is employed, according to the formula::

    y = bdtrc( k, n, p ) = incbet( k+1, n-k, p )

The arguments must be positive, with p ranging from 0 to 1.


Accuracy
--------

Tested at random points (a, b, p).

+----------+------+--------+---------------+
|          | a, b |        |relative error |
+----------+------+--------+-------+-------+
|arithmetic|domain|# trials|peak   |rms    |
+==========+======+========+=======+=======+
|For p between 0.001 and 1                 |
+----------+------+--------+-------+-------+
|IEEE      |0, 100|100000  |6.7e-15|8.2e-16|
+----------+------+--------+-------+-------+
|For p between 0 and .001                  |
+----------+------+--------+-------+-------+
|IEEE      |0, 100|100000  |1.5e-13|2.7e-15|
+----------+------+--------+-------+-------+

Error messages
--------------

+------------+-------------------+--------------+
|message     |condition          |value returned|
+============+===================+==============+
|bdtrc domain|x < 0, x > 1, n < k|0.0           |
+------------+-------------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#bdtrc
