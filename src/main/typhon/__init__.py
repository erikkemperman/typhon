from sys import version_info

if version_info < (3, 5):
   raise ImportError('Typhon requires Python version 3.5')


from . import about


class myclass:
    """
    Useless class
    """
    pass
