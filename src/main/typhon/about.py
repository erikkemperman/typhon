"""
Bla bla
"""

print('yay')


def test(arg: str) -> bool:
    """Hello

    >>> 1 + 13
    14

    :param arg: An argument
    :return: Return the resulting value
    """
    return arg == 'foo'


def foo(a: int, b: int) -> int:
    """Bar

    :param a: A number
    :type a: int
    :param b: A number
    :type b: int
    :return: Return also a number
    :rtype: int
    """
    return a + b



