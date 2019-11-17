import asyncio


async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')


async def main():
    event = asyncio.Event()

    waiter_task = asyncio.create_task(waiter(event))

    print('await waiter')
    await asyncio.sleep(1)
    event.set()
    print('set event')

    await waiter_task

if __name__ == '__main__':
    asyncio.run(main())
