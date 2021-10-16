from .client import Client
from .exceptions import HTTPException

METRIC = "C"
IMPERIAL = "F"
__version__ = "0.3.6"
__all__ = ("Client", "METRIC", "IMPERIAL", "HTTPException", "__version__")
