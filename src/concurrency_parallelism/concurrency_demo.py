# concurrency_demo.py
import threading
import multiprocessing
import time


# ✅ External function required for multiprocessing on Windows
def process_task(num, results):
    time.sleep(0.1)  # Simulate work
    result = num * num
    results.append(result)


class ThreadWorker:
    def __init__(self):
        self.results = []
        self.lock = threading.Lock()

    def task(self, num):
        time.sleep(0.1)
        result = num * num
        with self.lock:
            self.results.append(result)

    def run(self, numbers):
        threads = []
        for num in numbers:
            t = threading.Thread(target=self.task, args=(num,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return self.results


class ProcessWorker:
    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.results = self.manager.list()

    def run(self, numbers):
        processes = []
        for num in numbers:
            # 🔁 Use the external function instead of self.task
            p = multiprocessing.Process(target=process_task, args=(num, self.results))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        return list(self.results)
