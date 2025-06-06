# ptufile/__init__.py

from .ptufile import *
from .ptufile import __all__, __doc__, __version__

# constants are repeated for documentation

__version__ = __version__
"""Ptufile version string."""

T2_RECORD_DTYPE = T2_RECORD_DTYPE
"""Numpy dtype of decoded T2 records."""

T3_RECORD_DTYPE = T3_RECORD_DTYPE
"""Numpy dtype of decoded T3 records."""


def _set_module() -> None:
    """Set __module__ attribute for all public objects."""
    globs = globals()
    module = globs['__name__']
    for item in __all__:
        obj = globs[item]
        if hasattr(obj, '__module__'):
            obj.__module__ = module


_set_module()
