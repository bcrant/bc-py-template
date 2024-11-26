"""{{ ookiecutter.package_name }}/core/cmd.py"""

from {{ cookiecutter.package_name }} import (
    env,
    log,
    {{ cookiecutter.package_name.upper() }}_PREFIX,
)


with env.prefixed({{ cookiecutter.package_name.upper() }}_PREFIX):
    {{ cookiecutter.package_name.upper() }}_FOO = env("FOO")
    {{ cookiecutter.package_name.upper() }}_BAR = env("BAR")


def run_{{ ookiecutter.package_name }}(foo: str) -> None:
    """
    Run {{ ookiecutter.package_name }}.

    Args:
        foo: str   A description or typehint of foo
    Returns:
        None
    """
    log.info("Run {{ ookiecutter.package_name }} starting...")
    #
    # Do some stuff
    #
    log.info("Run {{ ookiecutter.package_name }} ended.")
