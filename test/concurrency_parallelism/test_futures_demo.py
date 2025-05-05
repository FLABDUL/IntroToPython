# test_futures_demo.py

from concurrency_parallelism.futures_demo import run_with_threads, run_with_processes


def test_run_with_threads():
    results = run_with_threads()
    assert results == [0, 1, 2, 3]


def test_run_with_processes():
    results = run_with_processes()
    assert len(results) == 4
    assert all(isinstance(r, int) for r in results)
