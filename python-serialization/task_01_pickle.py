import pickle
import os  # Imported os for safe file deletion in testing (optional)


class CustomObject:
    """A custom class for demonstrating serialization using the pickle module."""

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject with specified attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object’s attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current object instance and saves it to a file using pickle."""
        try:
            # Open the file in binary write mode ('wb')
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a pickled file."""
        try:
            # Open the file in binary read mode ('rb')
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
        except Exception:
            # Handles malformed files or other loading errors
            return None

