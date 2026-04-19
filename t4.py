import time
import random

def task4(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            pass


def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        t = measure_time(task4, n)
        print(n, round(t, 5))