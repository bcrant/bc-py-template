"""{{ cookiecutter.package_name }}/)__init__.py"""

import logging
from environs import Env
from . import _log, _version

#
# ENV
#

# Load environment variables from runtime and/or read from dotenv files
env = Env(expand_vars=True)
env.read_env(verbose=True)

# Set module environs prefixes, e.g. AWS_PREFIX, POSTGRES_PREFIX
{{ cookiecutter.package_name.upper() }}_PREFIX = "{{ cookiecutter.package_name.upper() }}_"


#
# LOGGING
#

# Initialize logger
log = _log.setup_logging(app_name="{{ cookiecutter.package_name }}", json_fmt=False, debug=True)

# Demote noisy third-party loggers
logging.getLogger("botocore.credentials").setLevel(logging.ERROR)
logging.getLogger("ddtrace").setLevel(logging.CRITICAL)
logging.getLogger("datadog_lambda").setLevel(logging.CRITICAL)
logging.getLogger("paramiko.transport").setLevel(logging.ERROR)


#
# PACKAGING
#
__version__ = _version.get_versions()["version"]
