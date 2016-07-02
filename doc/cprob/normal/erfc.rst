Complementary error function
============================

.. py:function:: erfc(x)

    Computes ``1 - erf(x)`` in a numerically stable way.

    :param float x: a real scalar.


Description
-----------


.. math::
    1 - \mathrm{erf}(x) =
    \mathrm{erfc}(x) = \frac{2}{\sqrt{\pi}} \int_x^{\infty} \exp{(-t^2)}dt

For small :math:`x`, ``erfc(x) = 1 - erf(x)``; otherwise rational
approximations are computed.

A special function :py:func:`expx2` is used to suppress error amplification
in computing :math:`\exp{(-x^2)}`.

Accuracy
--------

+-----------+------------+------------+------------+-----------+
|                                     |      Relative error    |
+-----------+------------+------------+------------+-----------+
|arithmetic |  domain    |  # trials  |    peak    |     rms   |
+===========+============+============+============+===========+
|   IEEE    | 0, 26.6417 |  30000     |   1.3e-15  |   2.2e-16 |
+-----------+------------+------------+------------+-----------+

Error messages
--------------

+----------------+-----------------------+--------------+
|message         |condition              |value returned|
+================+=======================+==============+
|erfc underflow  | x > 9.231948545 (DEC) | 0.0          |
+----------------+-----------------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#erfc
