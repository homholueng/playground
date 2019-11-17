import asyncio


async def lock_competitor(n, lock):
    print(f"competitor{n} try to get lock")

    async with lock:
        print(f"competitor{n} get the lock")
        print(f"competitor sleep for {n} seconds...")
        await asyncio.sleep(n)
        print(f"competitor{n} wake up!")
        print(f"competitor{n} give up the lock")


async def main():
    lock = asyncio.Lock()
    await asyncio.gather(*[lock_competitor(n, lock) for n in range(1, 5)])


if __name__ == '__main__':
    asyncio.run(main())
