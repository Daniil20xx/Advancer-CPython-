import multiprocessing

def worker_receiver(conn):
    number = conn.recv()
    result = number ** 2
    conn.send(result)
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=worker_receiver, args=(child_conn,))
    p.start()

    number = 7
    print(f"Sender отправил: {number}")

    parent_conn.send(number)

    result = parent_conn.recv()
    print(f"Sender получил результат: {result}")

    p.join()

''' Output:
python.exe .\task4.py
Sender отправил: 7
Sender получил результат: 49
'''