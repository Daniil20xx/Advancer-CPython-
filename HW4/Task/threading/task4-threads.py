import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def process_one():
    with lock_a:
        print("[P1] Захватил Lock A, думаю...")
        time.sleep(0.5)

        print("[P1] Пытаюсь захватить Lock B...")

        with lock_b:
            print("[P1] Успех! Выполнил задачу.")

def process_two():
    with lock_a:
        print("[P2] Захватил Lock A, думаю...")
        time.sleep(0.5)

        print("[P2] Пытаюсь захватить Lock B...")

        with lock_b:
            print("[P2] Успех! Выполнил задачу.")

t1 = threading.Thread(target=process_one)
t2 = threading.Thread(target=process_two)

t1.start()
t2.start()

t1.join()
t2.join()

print("Программа завершена without deadlock!!!")

''' Output:
python.exe .\task4-threads.py
[P1] Захватил Lock A, думаю...
[P1] Пытаюсь захватить Lock B...
[P1] Успех! Выполнил задачу.
[P2] Захватил Lock A, думаю...
[P2] Пытаюсь захватить Lock B...
[P2] Успех! Выполнил задачу.
Программа завершена without deadlock!!!
'''