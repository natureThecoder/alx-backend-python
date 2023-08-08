#!/usr/bin/env python3
"""A coroutine called async_generator that takes no arguments"""


import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops 10x and yield a random number b/w 0 & 10"""
    for i in range(10):
        await asyncio.sleep(1)

        yield uniform(0, 10)
