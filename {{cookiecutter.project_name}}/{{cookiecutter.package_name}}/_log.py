"""{{ cookiecutter.package_name }}/)_log.py"""

import logging
from typing import Dict, List

import json_log_formatter


LOG_FMT = (
    "%(asctime)-20s [%(levelname)-8s] %(name)-24s %(pathname)s:%(lineno)-4s %(message)s"
)


class PathTruncatingFormatter(logging.Formatter):
    """Truncate path of file where log message is produced."""

    def format(self, record):
        """
        # Logging Formatter subclass to truncate the pathname.
        # This enables the log components to be evenly aligned.
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


class TracingJSONLogFormatter(json_log_formatter.JSONFormatter):
    """
    Tracing JSON log formatter to convert log messages to JSON.
    """

    _log_builtin_attrs = (
        "args",
        "asctime",
        "created",
        "exc_info",
        "exc_text",
        "filename",
        "funcName",  # 'levelname',
        "levelno",  # 'lineno',
        # 'module',
        "msecs",
        "message",
        "msg",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "stack_info",
        "thread",
        "threadName",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extra_from_record(self, record: Dict) -> Dict:
        """
        Cleans up the log message using the provided self._log_builtin_attrs

        :param record:
        :return:
        """
        return {
            attr_name: record.__dict__[attr_name]
            for attr_name in record.__dict__
            if attr_name not in self._log_builtin_attrs
        }

    def to_json(self, record: Dict) -> str:
        """
        Converts the log message to JSON.

        :param record:
        :return:
        """
        record["level"] = record["levelname"]
        record["line_number"] = record["lineno"]
        del record["levelname"]
        del record["lineno"]
        return self.json_lib.dumps(record, default=str)


def setup_logging(
    app_name: str = None,
    modules: List[str] = [],
    debug: bool = True,
    json_fmt: bool = True,
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
        json_fmt:       Defaults to True, applies TracingJsonLogFormatter
                        False applies string PathTruncatingFormatter

    Returns:
        logger object with JSON formatting.
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
        if json_fmt:
            stream_handler.setFormatter(TracingJSONLogFormatter())
        else:
            stream_handler.setFormatter(PathTruncatingFormatter(LOG_FMT))
        logger.addHandler(stream_handler)
    return logging.getLogger(app_name)
