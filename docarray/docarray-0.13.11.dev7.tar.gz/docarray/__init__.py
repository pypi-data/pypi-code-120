__version__ = '0.13.11.dev7'

import os

from .document import Document
from .array import DocumentArray
from .dataclasses import dataclass, field

if 'DA_NO_RICH_HANDLER' not in os.environ:
    from rich.traceback import install

    install()
