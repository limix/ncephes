Cumulative distribution function
================================
.. py:function:: chdtr(k, x)

    Returns the area under the left hand tail (from 0 to x)
    of the Chi square probability density function with
    k degrees of freedom.

    :param int k: degrees of freedom
    :param float x: positive Chi square variable

Description
-----------

.. math::
    P(x~|~k) = \frac{1}{\Gamma (k/2)} \int_{0}^{x/2} t^{k/2-1} e^{-t} dt

The incomplete gamma integral is used according to the formula::

    chdtr(k, x) = igam(k/2, x/2)

The arguments must both be positive.

Accuracy
--------

See :py:func:`igam` for accuracy.

Error messages
--------------

+------------+--------------+--------------+
|message     |condition     |value returned|
+============+==============+==============+
|chdtr domain|x < 0 or v < 1|0             |
+------------+--------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#chdtr
