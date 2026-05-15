import asyncio

async def slow_api_call():
    await asyncio.sleep(5)
    return "Success"

async def main():

    try:
        result = await asyncio.wait_for(
            slow_api_call(),
            timeout=2
        )

        print(result)

    except asyncio.TimeoutError:
        print("API запрос занял слишком много времени!")

asyncio.run(main())

''' Output:
ython.exe .\task2.py
API запрос занял слишком много времени!
'''