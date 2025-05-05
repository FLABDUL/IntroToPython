# asyncio_demo.py
import asyncio
import time

class AsyncWorker:
    """
    Demonstrates asynchronous programming using asyncio.

    Pros:
    - Lightweight concurrency for I/O-bound tasks
    - Avoids GIL-related issues with multithreading

    Cons:
    - Not useful for CPU-heavy tasks
    - Must use async-compatible libraries

    This class simulates I/O work using asyncio.sleep
    """
    async def task(self, num):
        await asyncio.sleep(0.1)  # Simulate I/O
        return num * num

    async def run(self, numbers):
        # Create coroutines for all numbers
        tasks = [self.task(num) for num in numbers]
        # Run all coroutines concurrently
        results = await asyncio.gather(*tasks)
        return results
