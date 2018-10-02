Inverse of the survival function
================================
.. py:function:: chdtri(k, y)

    Finds the Chi-square argument x such that the integral
    from x to infinity of the Chi-square density is equal
    to the given cumulative probability y.

    :param int k: degrees of freedom
    :param float y: cumulative probability

Description
-----------

This is accomplished using the inverse gamma integral function and the
relation::

    x/2 = igami(k/2, y)

Accuracy
--------

See :py:func:`igami` for accuracy.

Error messages
--------------

+-------------+--------------+--------------+
|message      |condition     |value returned|
+=============+==============+==============+
|chdtri domain|y < 0 or y > 1|0             |
+             +--------------+              +
|             |k < 1         |              |
+-------------+--------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#chdtri
