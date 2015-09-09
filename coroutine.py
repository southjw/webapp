import asyncio

@asyncio.coroutine
def test():
    print("test start!...")
    r = yield from asyncio.sleep(1)
    print("test end!...")

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from test()
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
