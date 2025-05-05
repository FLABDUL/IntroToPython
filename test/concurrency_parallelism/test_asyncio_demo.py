# test_asyncio_demo.py
import pytest

from concurrency_parallelism.asyncio_demo import AsyncWorker


@pytest.mark.asyncio
async def test_async_worker():
    worker = AsyncWorker()
    result = await worker.run([1, 2, 3, 4])
    expected = [1, 4, 9, 16]
    assert result == expected
