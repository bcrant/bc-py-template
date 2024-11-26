"""{{ cookiecutter.project_name }}/cli.py"""

import click

from {{ cookiecutter.package_name }}.core.cmd import run_{{ cookiecutter.package_name }}
from . import log


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """Init click cli."""
    log.debug(f"ctx {type(ctx)}: {vars(ctx)}")


@click.command()
@click.option("-j", "--job-name", type=str)
def run_job(job_name):
    """
    Ingest {{ cookiecutter.package_name }} data

    Args:
        job_name: str   One of '{{ cookiecutter.package_name }}.job_name1', '{{ cookiecutter.package_name }}.job_name2', '{{ cookiecutter.package_name }}.job_name3'
    Returns:
        None
    """
    run_{{ cookiecutter.package_name }}(job_name)


if __name__ == "__main__":
    main()
