#!/usr/bin/python3

def make_multiplier(multiplier: float) -> float:
    """returns multiplied float"""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
