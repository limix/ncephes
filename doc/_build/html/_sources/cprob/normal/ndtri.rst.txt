Inverse of the cumulative distribution function
===============================================

.. py:function:: ndtri(y)

    Returns the argument ``x`` for which the area under the
    Gaussian probability density function (integrated from
    minus infinity to ``x``) is equal to ``y``.

    :param float y: area under the curve.

Description
-----------

For small arguments :math:`0 < y < \exp{(-2)}`, the program computes
:math:`z = \sqrt{-2.0 * \log{y}}`;  then the approximation is

.. math:: x = z - \log{(z)}/z  - (1/z) P(1/z) / Q(1/z).

There are two rational functions P/Q, one for :math:`0 < y < \exp{(-32)}`
and the other for :math:`y` up to :math:`\exp{(-2)}`.  For larger arguments,
:math:`w = y - 0.5`, and

.. math:: x/\sqrt{2\pi} = w + w^3 R(w^2)/S(w^2).

Accuracy
--------

+-----------+---------------+------------+------------+-----------+
|                                        |  Relative error        |
+-----------+---------------+------------+------------+-----------+
|arithmetic |  domain       |  # trials  |    peak    |     rms   |
+===========+===============+============+============+===========+
|   DEC     | 0.125, 1      |   5500     |   9.5e-17  |   2.1e-17 |
+-----------+---------------+------------+------------+-----------+
|   DEC     | 6e-39, 0.135  |  3500      |   5.7e-17  |   1.3e-17 |
+-----------+---------------+------------+------------+-----------+
|   IEEE    | 0.125, 1      |   20000    |   7.2e-16  |   1.3e-16 |
+-----------+---------------+------------+------------+-----------+
|   IEEE    | 3e-308, 0.135 |  50000     |   4.6e-16  |   9.8e-17 |
+-----------+---------------+------------+------------+-----------+


Error messages
--------------

+----------------+------------+--------------+
|message         |condition   |value returned|
+================+============+==============+
|ndtri domain    |   x <= 0   | -MAXNUM      |
+----------------+------------+--------------+
|ndtri domain    |   x >= 1   |  MAXNUM      |
+----------------+------------+--------------+

Reference: http://www.netlib.org/cephes/doubldoc.html#ndtri
