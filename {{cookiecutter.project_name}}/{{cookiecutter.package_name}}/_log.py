"""{{ cookiecutter.package_name }}/_log.py"""

import logging
from typing import Dict, List


LOG_FMT = (
    "%(asctime)-20s [%(levelname)-8s] %(name)-24s %(pathname)s:%(lineno)-4s %(message)s"
)


class PathTruncatingFormatter(logging.Formatter):
    """Truncate path of file where log message is produced."""

    def format(self, record):
        """
        Logging Formatter subclass to truncate the pathname.
        This enables the log components to be evenly aligned.
        """
        if "pathname" in record.__dict__.keys():
            full_path = record.pathname
            str_size = 20
            if len(full_path) >= str_size:
                trunc_str_size = -1 * str_size - 3
                trunc_path = "..." + str(full_path[trunc_str_size:])
            elif len(full_path) < str_size:
                trunc_path = full_path.ljust(str_size - len(full_path))
            else:
                trunc_path = full_path
            record.pathname = trunc_path
        return super(PathTruncatingFormatter, self).format(record)


def setup_logging(
    app_name: str = None,
    modules: List[str] = [],
    debug: bool = True,
):
    """
    Sets up global logging for provided list of modules and the app_name provided

    Args:
        app_name:       Name to use for setting up logger
        modules:        List of modules to apply PathTruncatingFormatter to.
                        Common loggers that can be enabled:
                            boto3 | boto3.resources.factory
                            botocore | botocore.auth
                            fastapi | fastapi.logger
                            s3transfer
                            urllib3.connectionpool
                            uvicorn.access | uvicorn.error
        debug:          Defaults to True, can be disabled in Prod

    Returns:
        logger instance.
    """

    level = logging.DEBUG if debug else logging.INFO
    if app_name and app_name not in modules:
        modules.append(app_name)
    if not app_name and not modules:
        modules.append("root")
    for module_name in modules:
        logger = logging.getLogger(module_name)
        logger.setLevel(level)
        logger.propagate = False
        if logger.hasHandlers():
            logger.handlers.clear()
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(PathTruncatingFormatter(LOG_FMT))
        logger.addHandler(stream_handler)
    return logging.getLogger(app_name)
