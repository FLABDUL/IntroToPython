import pytest

from src.demo.CountUpTo import CountUpTo


def test_counting_sequence():
    """
    Test that CountUpTo correctly counts from 1 to max_count.
    """
    counter = CountUpTo(5)
    expected = [1, 2, 3, 4, 5]
    result = list(counter)
    assert result == expected

def test_single_value():
    """
    Test counting up to 1 (edge case).
    """
    counter = CountUpTo(1)
    expected = [1]
    result = list(counter)
    assert result == expected

def test_zero_max_count():
    """
    Test counting up to 0 should produce an empty list.
    """
    counter = CountUpTo(0)
    expected = []
    result = list(counter)
    assert result == expected

def test_manual_iteration():
    """
    Test manual iteration using next().
    """
    counter = CountUpTo(3)
    iterator = iter(counter)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    with pytest.raises(StopIteration):
        next(iterator)  # Should raise after reaching the limit
