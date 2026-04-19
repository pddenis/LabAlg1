import time
import random
import tracemalloc

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

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

def measure_memory(func, data):
    tracemalloc.start()
    func(data)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


sizes = [100, 1000, 5000, 10000]
print("Размер | Время (сек) | Память (кб)")
print("-" * 35)    
for n in sizes:
    arr = generate_array(n)
    t = measure_time(quicksort, arr)
    m = measure_memory(quicksort, arr)/1024
    print(f"{n:6} | {round(t, 5):11} | {round(m, 2):9}")