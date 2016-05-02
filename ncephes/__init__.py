from __future__ import absolute_import
import pkg_resources
from .lib import get_include

__version__ = pkg_resources.get_distribution("ncephes").version
