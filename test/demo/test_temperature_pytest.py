import pytest

from src.demo.Temperature import Temperature


@pytest.mark.parametrize(
    "celsius, expected_fahrenheit",
    [
        (0, 32.0),
        (100, 212.0),
        (37, 98.6),
        (-40, -40.0),   # Fun fact: -40° is the same in C and F!
    ]
)
def test_celsius_to_fahrenheit(celsius, expected_fahrenheit):
    temp = Temperature(celsius)
    assert round(temp.fahrenheit, 2) == expected_fahrenheit


@pytest.mark.parametrize(
    "fahrenheit, expected_celsius",
    [
        (32, 0),
        (212, 100),
        (98.6, 37),
        (-40, -40),
    ]
)
def test_fahrenheit_to_celsius(fahrenheit, expected_celsius):
    temp = Temperature(0)  # initial value doesn't matter
    temp.fahrenheit = fahrenheit
    assert round(temp.celsius, 2) == expected_celsius


def test_setting_celsius():
    temp = Temperature(10)
    temp.celsius = 50
    assert temp.celsius == 50
    assert round(temp.fahrenheit, 2) == 122.00


def test_below_absolute_zero():
    temp = Temperature(0)
    with pytest.raises(ValueError):
        temp.celsius = -300  # Should raise an error
