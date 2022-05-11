""" MCLI Versioning """
__version_major__ = 0
__version_minor__ = 1
__version_patch__ = 2
__version_extras__ = ''
__version__ = f'v{__version_major__}.{__version_minor__}.{__version_patch__}{__version_extras__}'


def print_version(**kwargs) -> int:
    del kwargs
    print(__version__)
    return 0
