import multiprocessing
import os

def worker(q):
    message = q.get()
    print(f"Процесс PID={os.getpid()} получил сообщение: {message}")

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    queue.put("Привет из главного процесса!")

    p.join()


'''
Output:
python.exe .\task3.py
Процесс PID=2776 получил сообщение: Привет из главного процесса!
'''