#!/usr/bin/env python3
''' Description: Add annotations to the below function’s parameters and
                 return values with the appropriate types
    Parameters: lst: Iterable[Sequence]
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
