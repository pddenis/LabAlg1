import time
import random

def task2(arr):
    max1 = 0
    max2 = 0
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        else:
            if i > max2:
                max2 = i
    return max1, max2


def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start


sizes = [100, 1000, 5000, 10000]
for n in sizes:
    arr = generate_array(n)
    t = measure_time(task2, arr)
    print(n, round(t, 7))