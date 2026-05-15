import asyncio
import random

async def fetch_url(url, semaphore):
    async with semaphore:
        print(f"[Запрос] Проверка {url} началась")
        await asyncio.sleep(random.randint(1, 3))
        print(f"[Готово] {url} проверен")


async def main():
    sem = asyncio.Semaphore(3)
    urls = [
        f"https://site_{i}.com"
        for i in range(1, 21)
    ]
    tasks = [
        fetch_url(url, sem)
        for url in urls
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())

''' Output:
python.exe .\task3.py
[Запрос] Проверка https://site_1.com началась
[Запрос] Проверка https://site_2.com началась
[Запрос] Проверка https://site_3.com началась
[Готово] https://site_2.com проверен
[Запрос] Проверка https://site_4.com началась
[Готово] https://site_1.com проверен
[Готово] https://site_3.com проверен
[Запрос] Проверка https://site_5.com началась
[Запрос] Проверка https://site_6.com началась
[Готово] https://site_4.com проверен
[Запрос] Проверка https://site_7.com началась
[Готово] https://site_5.com проверен
[Готово] https://site_6.com проверен
[Готово] https://site_7.com проверен
[Запрос] Проверка https://site_8.com началась
[Запрос] Проверка https://site_9.com началась
[Запрос] Проверка https://site_10.com началась
[Готово] https://site_10.com проверен
[Запрос] Проверка https://site_11.com началась
[Готово] https://site_9.com проверен
[Запрос] Проверка https://site_12.com началась
[Готово] https://site_8.com проверен
[Запрос] Проверка https://site_13.com началась
[Готово] https://site_12.com проверен
[Готово] https://site_11.com проверен
[Запрос] Проверка https://site_14.com началась
[Запрос] Проверка https://site_15.com началась
[Готово] https://site_14.com проверен
[Запрос] Проверка https://site_16.com началась
[Готово] https://site_13.com проверен
[Готово] https://site_15.com проверен
[Запрос] Проверка https://site_17.com началась
[Запрос] Проверка https://site_18.com началась
[Готово] https://site_17.com проверен
[Запрос] Проверка https://site_19.com началась
[Готово] https://site_16.com проверен
[Готово] https://site_18.com проверен
[Запрос] Проверка https://site_20.com началась
[Готово] https://site_19.com проверен
[Готово] https://site_20.com проверен
'''