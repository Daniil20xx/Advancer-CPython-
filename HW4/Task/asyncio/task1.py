import asyncio
import time

async def fetch_data(data_id, delay):
    print(f"Старт загрузки Data-{data_id}")

    await asyncio.sleep(delay)

    return f"Data-{data_id}"

async def main():
    start_time = time.perf_counter()

    results = await asyncio.gather(
        fetch_data(1, 1),
        fetch_data(2, 2),
        fetch_data(3, 3)
    )

    end_time = time.perf_counter()

    print(f"Результаты: {results}")
    print(f"Затрачено времени: {end_time - start_time:.2f} сек")

asyncio.run(main())

''' Output:
python.exe .\task1.py        
Старт загрузки Data-1
Старт загрузки Data-2
Старт загрузки Data-3
Результаты: ['Data-1', 'Data-2', 'Data-3']
Затрачено времени: 3.01 сек
'''