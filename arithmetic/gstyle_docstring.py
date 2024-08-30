def example(arg1, arg2):
    """Division of two reals.

    This function is only to show how we can format docstrings using
    Google Style Guide.

    Args:
        - arg1 (float): The first value.
        - arg2 (float): The second value, cannot be Nul.

    Returns:
        float: Division arg1/arg2.

    Raises:
        ZeroDivisionError: if arg2 is zero.

    Example:
        >>> import template
        >>> a = MainClass()
        >>> a.example(6,2)
        1.5

    Todo:
        Check that arg2 is non zero, and throw an exception.
"""
