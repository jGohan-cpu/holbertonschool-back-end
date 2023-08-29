#!/bin/usr/python3

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes string int or float and returns tupple"""
    square = v ** 2
    return k, square
