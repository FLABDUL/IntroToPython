# test_gil_demo.py

from concurrency_parallelism.gil_demo import ThreadedGILDemo, ProcessGILDemo

def test_threaded_gil_demo():
    demo = ThreadedGILDemo(count=1_000_000, num_threads=4)
    result = demo.run()

    assert len(result["results"]) == 4
    assert all(isinstance(r, int) for r in result["results"])
    assert result["time_taken"] > 0


def test_process_gil_demo():
    demo = ProcessGILDemo(count=1_000_000, num_processes=4)
    result = demo.run()

    assert len(result["results"]) == 4
    assert all(isinstance(r, int) for r in result["results"])
    assert result["time_taken"] > 0


def test_process_vs_thread_speed():
    thread_demo = ThreadedGILDemo(count=5_000_000, num_threads=4)
    process_demo = ProcessGILDemo(count=5_000_000, num_processes=4)

    thread_result = thread_demo.run()
    process_result = process_demo.run()

    # In most cases, multiprocessing will be faster for CPU-bound work
    assert process_result["time_taken"] < thread_result["time_taken"] * 1.5
