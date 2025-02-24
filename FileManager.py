import struct


class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_text(self, text):
        """Writes text to a file."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(text)

    def read_text(self):
        """Reads text from a file."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write_binary(self, data):
        """Writes binary data to a file."""
        with open(self.file_path, 'wb') as file:
            file.write(data)

    def read_binary(self):
        """Reads binary data from a file."""
        with open(self.file_path, 'rb') as file:
            return file.read()

    def write_struct(self, format_string, *values):
        """Writes structured binary data using struct."""
        packed_data = struct.pack(format_string, *values)
        self.write_binary(packed_data)

    def read_struct(self, format_string):
        """Reads structured binary data using struct."""
        data = self.read_binary()
        return struct.unpack(format_string, data)


# Example usage
if __name__ == "__main__":
    file_manager = FileManager("example.txt")

    # Writing and reading text
    file_manager.write_text("Hello, world!")
    print("Text Read:", file_manager.read_text())

    # Writing and reading binary
    binary_data = b'\x00\x01\x02\x03'  # Sample binary data
    file_manager.write_binary(binary_data)
    print("Binary Read:", file_manager.read_binary())

    # Writing and reading structured binary data
    file_manager.write_struct('I f', 42, 3.14)  # Writing an integer and a float
    print("Structured Data Read:", file_manager.read_struct('I f'))
