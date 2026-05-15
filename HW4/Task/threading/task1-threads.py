import threading
import time

counter = 0

def increment():
    global counter

    for _ in range(100000):
        temp = counter
        time.sleep(0)
        counter = temp + 1

threads = [threading.Thread(target=increment) for _ in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Итоговый счетчик: {counter}")


''' Output:
python.exe .\task1-treads.py
Итоговый счетчик: 100000
'''