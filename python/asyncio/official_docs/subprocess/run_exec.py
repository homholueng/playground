import asyncio
import sys

program = """
import time
print('block sleep for 10 seconds ...')
time.sleep(10)
"""


async def main():
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', program,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

    print('sleep for 1 seconds...')
    await asyncio.sleep(1)

    stdout, stderr = await proc.communicate()

    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')


if __name__ == '__main__':
    asyncio.run(main())
