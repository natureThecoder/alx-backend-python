#!/usr/bin/env python3

"""A coroutine"""


import asyncio
from typing import List

wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_randomn times"""
    delays = []
    res = []

    for i in range(n):
        data = wait_random(max_delay)
        res.append(data)

    for task in asyncio.as_completed((res)):
        delay = await task
        delays.append(delay)

    return delays
