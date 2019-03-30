#!/usr/bin/env python3
from __future__ import annotations
from typing import Optional

# import requests


class FactoryMethod:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{ type(self).__name__ }()"

    @classmethod
    def factory_method(cls, success: bool = True) -> Optional[FactoryMethod]:
        if not success:
            return None
        return cls()


if __name__ == "__main__":
    # pylint: disable=invalid-name
    obj = FactoryMethod.factory_method()
    print(obj)
