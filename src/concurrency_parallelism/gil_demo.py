# gil_demo.py (updated)

import threading
import multiprocessing
import time


def cpu_heavy_task(count):
    total = 0
    for i in range(count):
        total += i * i
    return total


class ThreadedGILDemo:
    def __init__(self, count=10_000_000, num_threads=4):
        self.count = count
        self.num_threads = num_threads
        self.results = []

    def _thread_task(self):
        result = cpu_heavy_task(self.count)
        self.results.append(result)

    def run(self):
        start = time.time()
        threads = []
        for _ in range(self.num_threads):
            t = threading.Thread(target=self._thread_task)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        end = time.time()
        return {
            "results": self.results,
            "time_taken": end - start
        }


class ProcessGILDemo:
    def __init__(self, count=10_000_000, num_processes=4):
        self.count = count
        self.num_processes = num_processes

    def _process_task_wrapper(self, count):
        return cpu_heavy_task(count)

    def run(self):
        start = time.time()
        with multiprocessing.Pool(processes=self.num_processes) as pool:
            results = pool.map(self._process_task_wrapper, [self.count] * self.num_processes)
        end = time.time()
        return {
            "results": results,
            "time_taken": end - start
        }
