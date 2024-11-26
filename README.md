# BC Python Project Cookie Cutter Template

Generic Python project scaffolding with:
- black Formatter
- click CLI
- environs Environment variables
- pylint Linter
- pytest Testing
- setuptools Packaging
- versioneer Package versioning management

To use this tool, download the cookiecutter tool (after activating your virtual environment of choice):

~~~ bash
pip install cookiecutter
~~~

Use the GUI in Github to create a new project.

Use the tool to download the template and follow the prompts to setup your project. Make sure to copy in the project name, url and description from the previous step.

~~~ bash
cookiecutter git@git@github.com:bcrant/bc-py-template.git
~~~

Once the code is setup, setup git to use the repo:

~~~ bash
git init
git remote add origin git@<your url here>
git add .
git commit -m "Initial commit"
git push -u origin main
~~~
