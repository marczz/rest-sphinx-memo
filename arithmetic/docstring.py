def example(arg1, arg2):
    """ Divide two float numbers

    This is a Numpy docstring example.

    Parameters
    ----------
    arg1 : float
        the first value
    arg2 : float
        the second value

    Returns
    -------
    float
        arg1 divided by arg2

    Raises
    ------
    ZeroDivisionError
       when the second value is null.

    Examples
    --------
    >>> import template
    >>> a = MainClass()
    >>> a.example(6,2)
    1.5

    Warning
    -------
    arg2 must be non-zero.

    Notes
    -----
    Make sure we are using numpy syntax [1]_

    See Also
    --------
    :py:exc:`ZeroDivisionError`

    Todo
    ----
    We should use type inference

    References
    ----------
    .. [1] `Numpy Style Guide`_

    """
