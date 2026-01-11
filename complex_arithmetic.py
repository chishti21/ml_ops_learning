from complex_number import ComplexNumber
class ComplexArithmetic(ComplexNumber):

    # Default constructor
    def __init__(self, real=-1.0, imaginary=-1.0):
        super().__init__(real, imaginary)

    # Add two complex numbers
    def add(self, other):
        real = self._real + other._real
        imaginary = self._imaginary + other._imaginary
        return ComplexArithmetic(real, imaginary)

    # Multiply two complex numbers
    def multiply(self, other):
        real = (self._real * other._real) - (self._imaginary * other._imaginary)
        imaginary = (self._real * other._imaginary) + (self._imaginary * other._real)
        return ComplexArithmetic(real, imaginary)

    # Destructor
    def __del__(self):
        print("ComplexArithmetic object destroyed")