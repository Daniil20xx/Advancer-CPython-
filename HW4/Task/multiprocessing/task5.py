import multiprocessing
import os

def register_process(shared_dict):
    process_name = multiprocessing.current_process().name
    pid = os.getpid()

    shared_dict[process_name] = (pid, "Запиши меня в словарь")

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_dict = manager.dict()

    processes = []

    for i in range(3):
        p = multiprocessing.Process(
            target=register_process,
            args=(shared_dict,),
            name=f"Worker-{i}"
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for name, info in shared_dict.items():
        print(f"Процесс {name} (PID {info[0]}) записал: {info[1]}")

''' Output:
python.exe .\task5.py
Процесс Worker-0 (PID 7388) записал: Запиши меня в словарь
Процесс Worker-1 (PID 1224) записал: Запиши меня в словарь
Процесс Worker-2 (PID 13012) записал: Запиши меня в словарь
'''