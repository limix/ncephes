Error function
==============

.. py:function:: erf(x)

    :param float x: a real scalar.

Description
-----------

The integral is

.. math::
    \mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x \exp(-t^2) dt.

The magnitude of :math:`x` is limited to :math:`9.231948545` for DEC
arithmetic; :math:`1` or :math:`-1` is returned outside this range.

For :math:`0 <= |x| < 1`, :math:`\mathrm{erf}(x) = x * P4(x**2)/Q5(x**2)`;
otherwise :math:`\mathrm{erf}(x) = 1 - \mathrm{erfc}(x)`.

Accuracy
--------

+-----------+-----------+------------+------------+-----------+
|                                    |      Relative error    |
+-----------+-----------+------------+------------+-----------+
|arithmetic |  domain   |  # trials  |    peak    |     rms   |
+===========+===========+============+============+===========+
|   DEC     | 0, 1      |  14000     |   4.7e-17  |   1.5e-17 |
+-----------+-----------+------------+------------+-----------+
|   IEEE    | 0, 1      |  30000     |   3.7e-16  |   1.0e-16 |
+-----------+-----------+------------+------------+-----------+

Reference: http://www.netlib.org/cephes/doubldoc.html#erf
