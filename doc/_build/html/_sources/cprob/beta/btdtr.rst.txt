Cumulative distribution function
================================
.. py:function:: btdtr(a, b, x)

    Returns the area from zero to x under the beta density function.

   :param float a: a positive number
   :param float b: a positive number
   :param float x: any number within [0, 1]

See also :py:func:`incbet`.

Description
-----------

Returns the area from zero to x under the beta density function:

.. math::
    P(x~|~a, b) = \frac{\Gamma(a+b)}{\Gamma(a)+\Gamma(b)} \int_0^xt^{a-1}(1-t)^{b-1} dt

This function is identical to the incomplete beta integral function
:py:func:`incbet`.

The complemented function is:

    1 - P(1-x | a, b)  =  incbet( b, a, x )

Accuracy
--------

See :py:func:`incbet`.

Reference: http://www.netlib.org/cephes/doubldoc.html#btdtr
