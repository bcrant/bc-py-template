"""{{ cookiecutter.package_name }}/utils/foo_helpers.py"""

from {{ cookiecutter.package_name }} import log


def foo(bar: str) -> None:
    """Foo helper function"""
    log.info(f'bar {type(bar)}: {bar}')
    return
