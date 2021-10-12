import asyncio
import time

async def func1():
    print('任务一')
    await asyncio.sleep(1)
    print('任务一完成')

async def func2():
    print('任务二')
    await asyncio.sleep(2)
    print('任务二完成')

async def func3():
    print('任务三')
    await asyncio.sleep(3)
    print('任务三完成')

async def main():
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    print(time.time()-t1)