
import asyncio


@asyncio.coroutine
def hello(n):
    print('hello, world! ' + n)
    r = yield from asyncio.sleep(4)  # 等待 4 s 但是程序马上启动了第二个任务
    print('hello complete! ' + n)

async def hello(n):
    print('hello, world! ' + n)
    r = await asyncio.sleep(3)
    print('hello complete! ' + n)

loop = asyncio.get_event_loop()
task = asyncio.wait([hello('AAAAAA'), hello('BBBBBB')])
loop.run_until_complete(task)

