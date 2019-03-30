from glob import glob
import shutil
from typing import Dict, Any
from doit.task import clean_targets              # type: ignore

DOIT_CONFIG = {"verbosity": 2}
SRC_DIR = "{{cookiecutter.module_name}}"
TEST_DIR = "tests"

SRC = glob(f"{SRC_DIR}/**/*.py", recursive=True)
TESTS = glob(f"{TEST_DIR}/**/test_*.py")


def task_flake8() -> Dict[str, Any]:
    return {
        "actions": ("flake8",),
        "file_dep": SRC + [".flake8"]
    }


def task_pylint() -> Dict[str, Any]:
    cmd = "pylint " + " ".join(SRC + ["dodo.py"])
    return {
        "actions": (cmd,),
        "file_dep": SRC + [".pylintrc"]
    }


def task_mypy() -> Dict[str, Any]:
    cmd = "mypy --strict " + " ".join(SRC + ["dodo.py"])
    return {
        "actions": (cmd,),
        "file_dep": SRC
    }


def task_pytest() -> Dict[str, Any]:
    cmd = "pytest"
    return {
        "actions": (cmd,),
        "file_dep": SRC + TESTS
    }


def task_coverage() -> Dict[str, Any]:
    coverage_dir = "coverage"
    cmd = f"pytest --cov={SRC_DIR} --cov-report html:{coverage_dir}"

    def coverage_clean() -> None:
        shutil.rmtree(coverage_dir)

    return {
        "actions": (cmd,),
        "file_dep": SRC + TESTS,
        "targets": [f"{coverage_dir}/index.html"],
        "clean": [clean_targets, coverage_clean],
    }
