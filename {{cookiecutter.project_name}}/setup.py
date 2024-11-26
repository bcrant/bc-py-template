"""setup.py {{ cookiecutter.project_name }}"""

import codecs
import setuptools

import versioneer


requirements = None
try:
    with codecs.open("requirements.txt") as f:
        requirements = f.read().splitlines()
except:
    pass


setuptools.setup(
    name="{{ cookiecutter.project_name }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    packages=setuptools.find_packages(),
    {% if cookiecutter.include_cli == "y" -%}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.package_name }} = {{ cookiecutter.package_name }}.cli:run"
        ],
    },
    {%- endif %}
    keywords="{{ cookiecutter.project_name }}",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ]
)
