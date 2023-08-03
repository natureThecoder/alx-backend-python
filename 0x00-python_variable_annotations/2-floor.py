#!/usr/bin/env python3
''' Description:takes a float n as argument and returns the floor of the float
    Parameter: n: float
'''

def floor(n: float) -> float:
    if n >= 0:
        return int(n)
    else:
        return int(n) - 1
