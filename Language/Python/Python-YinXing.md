## 多线程与多进程

**多线程**是操作系统调度的最小单元，多线程编程允许一个进程内并发执行多个任务。线程之间共享进程的资源，比如内存和文件句柄，但有各自的**运行栈**。因此多线程编程可以在多核CPU系统提高性能。

### 创建线程

1. 通过`threading.Thread`函数创建线程。

   ```python
   import threading
   
   def task():
       print("Thread is running")
   
   thread = threading.Thread(target=task) # 创建线程对象
   thread.start() # 启动线程
   thread.join() # 等待子线程完成
   ```

   - `target`为需要执行的函数
   - `args`则是以元组形式传递给目标的参数

2. 通过继承`threading.Thread`类来创建线程。

   ```python
   import threading
   
   class MyThread(threading.Thread):
       def run(self):
           print("Thread is running")
   
   # 创建并启动线程
   thread = MyThread()
   thread.start()
   thread.join()
   ```

### 线程的常用方法

- `start()` 启动线程并调用target指定的函数
- `join()` 阻塞当前线程直到目标线程完成，通常用于主线程等待创建的子线程
- `is_alive()` 检查线程是否正在运行
- `getName()`和`setName(name)` 获取或设置线程的名称

```python
"""
file: find_prime_threading.py
find prime by using threading
date: 2024-11-21
author: cacc
"""

import threading
import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def count_primes(start, end, result, index):
    count = sum(1 for i in range(start, end) if is_prime(i))
    result[index] = count


def main():
    start_time = time.time()
    num_threads = 16
    limit = 10000000
    range_size = limit // num_threads
    threads = []
    result = [0] * num_threads # 创建一个长度为num_threads，初始元素为0的列表

    for i in range(num_threads):
        start = i * range_size
        end = (i + 1) * range_size if i != num_threads - 1 else limit
        thread = threading.Thread(target=count_primes, args=(start, end, result, i))
        threads.append(thread)
        thread.start() # 启动所有线程

    for thread in threads:
        thread.join()

    prime_count = sum(result)
    print(f"Prime count: {prime_count}")
    print(f"Time taken: {time.time() - start_time}")


if __name__ == "__main__":
    main()
```

```python
"""
file: find_prime_mutiprocessing.py
find primes by using mutiprocessing module
date: 2024-11-21
author: cacc
"""

import multiprocessing
import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def count_primes(start, end):
    return sum(1 for i in range(start, end) if is_prime(i))


def main():
    start_time = time.time()
    num_processes = 16
    limit = 10000000
    range_size = limit // num_processes
    pool = multiprocessing.Pool(num_processes)

    results = []
    for i in range(num_processes):
        start = i * range_size
        end = (i + 1) * range_size if i != num_processes - 1 else limit
        results.append(pool.apply_async(count_primes, (start, end)))

    pool.close()
    pool.join()

    prime_count = sum(result.get() for result in results)
    print(f"Prime count: {prime_count}")
    print(f"Time taken: {time.time() - start_time}")


if __name__ == "__main__":
    main()
```









列表

| 方法                  | 说明                                            |
| --------------------- | ----------------------------------------------- |
| list.append(x)        | 将元素x添加至列表尾部                           |
| list.extend(L)        | 将列表L中所有元素添加至列表尾部                 |
| list.insert(index, x) | 将元素x添加至指定位置                           |
| list.remove(x)        | 删除首次出现的指定元素                          |
| list.pop([index])     | 删除并返回列表指定位置的元素，默认最后一个元素  |
| list.clear()          | 删除列表中所有元素                              |
| list.index(x)         | 返回第一个值为x的元素下标，如果不存在则抛出异常 |
| list.count(x)         | 返回指定值x在列表中出现的次数                   |
| list.reverse()        | 对列表元素进行原地反转                          |
| list.sort()           | 对列表元素进行原地排序                          |
| list.copy()           | 返回列表的浅复制                                |