import threading
import queue
import time

def smart_worker(q, stop_event):
    while True:

        if stop_event.is_set():
            break

        try:
            task = q.get(timeout=0.5)

            if task is None:
                break

            print(f"[Worker] Выполняю задачу: {task}")

        except queue.Empty:
            continue

    print("[Worker] Поток полностью остановлен.")

task_queue = queue.Queue()
stop_signal = threading.Event()

worker_thread = threading.Thread(
    target=smart_worker,
    args=(task_queue, stop_signal)
)

worker_thread.start()

task_queue.put("Обработать данные пользователя")

time.sleep(1)

print("Подаем сигнал остановки через Event...")
stop_signal.set()

worker_thread.join()

print("Программа успешно завершена.")

''' Output:
python.exe .\task3-threads.py
[Worker] Выполняю задачу: Обработать данные пользователя
Подаем сигнал остановки через Event...
[Worker] Поток полностью остановлен.
Программа успешно завершена.
'''