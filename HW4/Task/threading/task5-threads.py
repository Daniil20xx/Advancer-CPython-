import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

def test_singleton():
    obj = DatabaseConnection()

    print(
        f"Поток {threading.current_thread().name} "
        f"получил объект ID: {id(obj)}"
    )

threads = []

for i in range(10):
    t = threading.Thread(
        target=test_singleton,
        name=f"T-{i}"
    )

    threads.append(t)
    t.start()

for t in threads:
    t.join()


''' Output:
python.exe .\task5-threads.py
Поток T-0 получил объект ID: 2548288293728
Поток T-1 получил объект ID: 2548288293728
Поток T-2 получил объект ID: 2548288293728
Поток T-3 получил объект ID: 2548288293728
Поток T-4 получил объект ID: 2548288293728
Поток T-5 получил объект ID: 2548288293728
Поток T-6 получил объект ID: 2548288293728
Поток T-7 получил объект ID: 2548288293728
Поток T-8 получил объект ID: 2548288293728
Поток T-9 получил объект ID: 2548288293728
'''