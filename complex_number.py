class ComplexNumber:
    # Default constructor
    def __init__(self, real=-1.0, imaginary=-1.0):
        self._real = real
        self._imaginary = imaginary

    # Copy constructor equivalent
    @classmethod
    def copy(cls, other):
        return cls(other._real, other._imaginary)

    # Display method
    def display(self):
        if self._imaginary < 0:
            print(f"{self._real} - i{abs(self._imaginary)}")
        else:
            print(f"{self._real} + i{self._imaginary}")