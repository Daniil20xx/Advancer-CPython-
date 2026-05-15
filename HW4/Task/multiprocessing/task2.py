from multiprocessing import Process, Value, Lock

def increment(shared_val, lock):
    for _ in range(1000):
        with lock:
            shared_val.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    lock = Lock()

    p1 = Process(target=increment, args=(counter, lock))
    p2 = Process(target=increment, args=(counter, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Итог: {counter.value}")


''' Output:
python.exe .\task2.py
Итог: 2000
'''