
import multiprocessing

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

import multiprocessing

def square(x):
    return x * x

if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)

    print(results)


''' Output:
python.exe .\task1.py
[1, 4, 9, 16, 25]
'''