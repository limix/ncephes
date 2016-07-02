Cumulative distribution function
================================

.. py:function:: ndtr(x)

    Returns the area under the Gaussian probability density
    function, integrated from minus infinity to ``x``.

    :param float x: a real scalar.

Description
-----------

Area under the curve:

.. math::
    \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^x \exp(-t^2/2) dt

Equivalently, we have::

    ndtr(x) = ( 1 + erf(z) ) / 2 =  erfc(z) / 2

where :math:`z = x/\sqrt{2}`. Computation is done via the functions
:py:func:`erf` and :py:func:`erfc` with care to avoid error amplification in
computing :math:`\exp{(-x^2)}`.

Accuracy
--------

+----------+------+--------+---------------+
|          |  x   |        |relative error |
+----------+------+--------+-------+-------+
|arithmetic|domain|# trials|peak   |rms    |
+==========+======+========+=======+=======+
|IEEE      |-13, 0| 30000  |1.3e-15|2.2e-16|
+----------+------+--------+-------+-------+

Error messages
--------------

+----------------+----------------+--------------+
|message         |condition       |value returned|
+================+================+==============+
|erfc underflow  |x > 37.519379347|0.0           |
+----------------+----------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#ndtr
