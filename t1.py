import time
import random

def task1(arr, a):
    fl=0
    for i in arr:
        if i == a:
            fl = 1
    return True if fl == 1 else False

def generate_num():
    a = random.randint(0, 10000)
    return a

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data, num):
    start = time.perf_counter()
    func(data, num)
    end = time.perf_counter()
    return end - start


sizes = [100, 1000, 5000, 10000]
for n in sizes:
    arr = generate_array(n)
    num = generate_num()
    t = measure_time(task1, arr, num)
    print(n, round(t, 7))