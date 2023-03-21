"""This module will be run everytime 'pytest' command is used globally"""

import sys
import pytest

from IPgen.const import PYTHON_VER, PYTEST_VER, PYTHON_VER_NOT_MATCHING, PYTEST_VER_NOT_MATCHING

# If Python or Pytest version isn't matching the requirements, no tests inside ./tests directory will be run

if "{0}.{1}".format(*sys.version_info) < PYTHON_VER:
    pytest.skip(reason=PYTHON_VER_NOT_MATCHING, allow_module_level=True)

if pytest.__version__ < PYTEST_VER:
    pytest.skip(reason=PYTEST_VER_NOT_MATCHING, allow_module_level=True)
