class Temperature:
    """
    A class to demonstrate @property and @setter decorators.
    It stores temperature in Celsius internally,
    but allows reading and writing it in Fahrenheit too.
    """
    def __init__(self, celsius):
        self._celsius = celsius  # "Private" variable by convention

    @property
    def celsius(self):
        """
        Getter for celsius.
        Allows reading temperature.celsius.
        """
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """
        Setter for celsius.
        Allows setting temperature.celsius = value.
        Also validates the input.
        """
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """
        Read-only property.
        Converts the celsius temperature to Fahrenheit.
        """
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """
        Allows setting temperature in Fahrenheit,
        and automatically converts it to Celsius.
        """
        self._celsius = (value - 32) * 5/9


# Example usage
if __name__ == "__main__":
    temp = Temperature(25)  # 25 degrees Celsius
    print(f"Temperature in Celsius: {temp.celsius}")  # 25
    print(f"Temperature in Fahrenheit: {temp.fahrenheit}")  # 77.0

    temp.celsius = 100  # Set new temperature in Celsius
    print(f"\nNew temperature in Celsius: {temp.celsius}")  # 100
    print(f"New temperature in Fahrenheit: {temp.fahrenheit}")  # 212.0

    temp.fahrenheit = 32  # Set new temperature using Fahrenheit
    print(f"\nAfter setting 32°F:")
    print(f"Temperature in Celsius: {temp.celsius}")  # 0.0
    print(f"Temperature in Fahrenheit: {temp.fahrenheit}")  # 32.0

    # Uncommenting below will raise a ValueError
    # temp.celsius = -300  # Below absolute zero
