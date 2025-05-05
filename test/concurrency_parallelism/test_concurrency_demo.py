# test_concurrency_demo.py
import pytest

from concurrency_parallelism.concurrency_demo import ThreadWorker, ProcessWorker


def test_thread_worker():
    worker = ThreadWorker()
    result = worker.run([1, 2, 3, 4])
    expected = [1, 4, 9, 16]
    assert sorted(result) == sorted(expected), "ThreadWorker failed"

def test_process_worker():
    worker = ProcessWorker()
    result = worker.run([1, 2, 3, 4])
    expected = [1, 4, 9, 16]
    assert sorted(result) == sorted(expected), "ProcessWorker failed"
