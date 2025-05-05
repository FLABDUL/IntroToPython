# futures_demo.py

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def cpu_bound(n):
    """Simulate a CPU-heavy task."""
    print(f"CPU task started: {n}")
    total = 0
    for i in range(10_000_000):
        total += i * i
    print(f"CPU task done: {n}")
    return total


def io_bound(n):
    """Simulate an I/O-heavy task."""
    print(f"I/O task started: {n}")
    time.sleep(2)  # Simulate I/O wait
    print(f"I/O task done: {n}")
    return n


def run_with_threads():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(io_bound, i) for i in range(4)]
        return [f.result() for f in futures]


def run_with_processes():
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_bound, i) for i in range(4)]
        return [f.result() for f in futures]
