import distutils.version
import logging
import sys

from gym import error
from gym.configuration import logger_setup, undo_logger_setup
from gym.utils import reraise

logger = logging.getLogger(__name__)

# Do this before importing any other gym modules, as most of them import some
# dependencies themselves.
def sanity_check_dependencies():
    hint = ' is a dependency of `gym` that should have been installed for you. If you directly cloned the GitHub repo, please run `pip install -r requirements.txt` first.'
    try:
        import numpy
    except ImportError as e:
        reraise(prefix='Failed to import package `numpy`',suffix='HINT: `numpy`'+hint)

    try:
        import requests
    except ImportError as e:
        reraise(prefix='Failed to import package `requests`',suffix='HINT: `requests`'+hint)

    try:
        import six
    except ImportError as e:
        reraise(prefix='Failed to import package `six`',suffix='HINT: `six`'+hint)

    if distutils.version.StrictVersion(numpy.__version__) < distutils.version.StrictVersion('1.10.4'):
        raise error.DependencyNotInstalled('You have `numpy` version {} installed, but gym requires at least 1.10.4. HINT: If you directly cloned the GitHub repo, please run `pip install -r requirements.txt` first.'.format(numpy.__version__))

    if distutils.version.StrictVersion(requests.__version__) < distutils.version.StrictVersion('2.0'):
        raise error.MujocoDependencyError('You have `requests` version {} installed, but gym requires at least 2.0. HINT: If you directly cloned the GitHub repo, please run `pip install -r requirements.txt` first.'.format(requests.__version__))

sanity_check_dependencies()
# We automatically configure a logger with a simple stderr handler. If
# you'd rather customize logging yourself, run undo_logger_setup.
#
# (Note: this needs to happen before importing the rest of gym, since
# we may print a warning at load time.)
logger_setup(logger)
del logger_setup

from gym.core import Env, Space
from gym.envs import make, spec
from gym.scoreboard.api import upload

__all__ = ["Env", "Space", "make", "spec", "upload"]
