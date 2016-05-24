Survival function
=================
.. py:function:: chdtrc(k, x)

    Returns the area under the right hand tail (from x to
    infinity) of the Chi square probability density function
    with k degrees of freedom.

    :param int k: degrees of freedom
    :param float x: positive Chi square variable

Description
-----------

The incomplete gamma integral is used according to the formula::

    chdtr(k, x) = igamc(k/2, x/2)

The arguments must both be positive.

Accuracy
--------

See :py:func:`igamc` for accuracy.

Error messages
--------------

+-------------+--------------+--------------+
|message      |condition     |value returned|
+=============+==============+==============+
|chdtrc domain|x < 0 or v < 1|0             |
+-------------+--------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#chdtrc
