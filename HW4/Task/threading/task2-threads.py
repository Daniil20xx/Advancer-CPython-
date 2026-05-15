import threading
import time
import random

def worker(worker_id, info):
    print(f"[Поток {worker_id}] Начинает Фазу 1...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"[Поток {worker_id}] Завершил Фазу 1")

    with info["lock"]:
        info["counter"] += 1

        if info["counter"] == 5:
            info["event"].set()

    info["event"].wait()

    print(f"[Поток {worker_id}] >>> ПЕРЕШЕЛ К ФАЗЕ 2")

shared_data = {
    "counter": 0,
    "lock": threading.Lock(),
    "event": threading.Event()
}

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i, shared_data))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nВсе потоки успешно прошли барьер.")


''' Output:
python.exe .\task2-threads.py
[Поток 0] Начинает Фазу 1...
[Поток 1] Начинает Фазу 1...
[Поток 2] Начинает Фазу 1...
[Поток 3] Начинает Фазу 1...
[Поток 4] Начинает Фазу 1...
[Поток 3] Завершил Фазу 1
[Поток 4] Завершил Фазу 1
[Поток 1] Завершил Фазу 1
[Поток 0] Завершил Фазу 1
[Поток 2] Завершил Фазу 1
[Поток 2] >>> ПЕРЕШЕЛ К ФАЗЕ 2
[Поток 3] >>> ПЕРЕШЕЛ К ФАЗЕ 2
[Поток 0] >>> ПЕРЕШЕЛ К ФАЗЕ 2
[Поток 1] >>> ПЕРЕШЕЛ К ФАЗЕ 2
[Поток 4] >>> ПЕРЕШЕЛ К ФАЗЕ 2

Все потоки успешно прошли барьер.
'''