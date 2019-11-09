import asyncio


def hello_world(loop):
    print('hello world')
    loop.stop()
    print('loop stop')


if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    loop.call_soon(hello_world, loop)

    print('run eventloop forever')
    loop.run_forever()
    print('close eventloop')
    loop.close()
