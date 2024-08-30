Division of two reals.

This function is only to show how we can format docstrings using
Google Style Guide.

:param - arg1: The first value.
:type - arg1: float
:param - arg2: The second value, cannot be Nul.
:type - arg2: float

:returns: Division arg1/arg2.
:rtype: float

:raises: :exc:`ZeroDivisionError` -- if arg2 is zero.

.. rubric:: Example

>>> import template
>>> a = MainClass()
>>> a.example(6,2)
1.5

.. todo:: Check that arg2 is non zero, and throw an exception.
