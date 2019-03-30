# cookiecutter-python-tools

Cookiecutter that has a few of the python tools configured:

  1. Doit - task runner
  2. flake8
  3. pylint
  4. mypy
  5. pytest
  6. pytest-cov

pytest-xdist is also included for the `pytest -f`

# Usage

_where {{cookiecutter.module_name}} is the name prompted installing cookiecutter_

```
cookiecutter gh:gshively/cookiecutter-python-tools

cd {{cookiecutter.module_name}}
pipenv install
pipenv shell
doit

```
