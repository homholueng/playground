import asyncio


async def coro1():
    raise Exception()


async def coro_n(num):
    print('coro', num)
    await asyncio.sleep(num)
    return num


async def main():
    results = await asyncio.gather(coro1(), coro_n(2), coro_n(3), return_exceptions=True)
    print(results)

if __name__ == '__main__':
    asyncio.run(main())
