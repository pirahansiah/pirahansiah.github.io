import asyncio
async def foo():
    print("1")
    await asyncio.sleep(2)
    print("2")
async def another():
    print("another")
async def main():
    await asyncio.gather(foo(),another())

asyncio.run(main())