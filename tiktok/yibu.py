# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 下午10:42
# @Author  : Wang Junling
# @File    : yibu.py
# @Software: PyCharm
import asyncio
import time
async def pr(name):
    print(name,'内')
    await [i for i in range(5*5555)]


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(0.0000000001)
        await asyncio.gather(pr(name))
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())