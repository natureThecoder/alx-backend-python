#!/usr/bin/env python3
"""A coroutine that collects 10 random
numbers from another coroutine"""


import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Returns a random number retrieved from a coroutine"""
    result = [i async for i in async_generator()]
    return result
