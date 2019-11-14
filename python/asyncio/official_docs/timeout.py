import asyncio


async def longtime_run():
    print('yay')
    await asyncio.sleep(36000)


async def main():
    try:
        await asyncio.wait_for(longtime_run(), timeout=2)
    except asyncio.TimeoutError:
        print('timeout!')


if __name__ == '__main__':
    asyncio.run(main())
