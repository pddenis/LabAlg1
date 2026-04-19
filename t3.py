import time
import random

def task3(arr, num, n):
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid  
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

def generate_array_num(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    num = arr[random.randint(0, n - 1)] 
    arr.sort() 
    return arr, num, n

def measure_time(func, data):
    start = time.perf_counter()
    func(*data) 
    end = time.perf_counter()
    return end - start

sizes = [100, 1000, 5000, 10000]
for n in sizes:
    data = generate_array_num(n)
    t = measure_time(task3, data)
    print(n, round(t, 7))