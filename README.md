# cookiecutter-python-tools

Cookiecutter that has a few of the python tools configured:

  #. Doit - task runner
  #. flake8
  #. pylint
  #. mypy
  #. pytest
  #. pytest-cov

pytest-xdist is also included for the `pytest -f`

# Usage

```
cookiecutter gh:gshively/cookiecutter-python-tools

cd {{cookiecutter.module_name}}
pipenv install
pipenv shell
doit

```
