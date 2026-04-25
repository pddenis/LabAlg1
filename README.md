№1
```python
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
```

Размер | Время (сек)
|:-------|-----------:|
100     |4e-06
1000    |1.75e-05
5000    |7.45e-05
10000   |0.0001317


№2
```python
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
```

Размер | Время (сек)
|:-------|-----------:|
100     |4.4e-06
1000    |2.57e-05
5000    |8.36e-05
10000   |0.0001824


№3
```python
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
```

Размер | Время (сек)
|:-------|-----------:|
100     |3.1e-06
1000    |1.9e-06
5000    |1.8e-06
10000   |3.3e-06


№4
```python
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
```

Размер | Время (сек)
|:-------|-----------:|
100     |4e-05
1000    |0.00628
5000    |0.17111
10000   |0.69324


№5
```python
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
```

Размер | Время (сек) | Память (кб)
|:-------|:-----------:|-------------:|
   100 |       7e-05 |       4.1
  1000 |      0.0007 |     34.74
  5000 |     0.00431 |    150.66
 10000 |     0.00889 |    302.91
