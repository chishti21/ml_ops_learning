from complex_arithmetic import ComplexArithmetic
import math

class ComplexAdvanced(ComplexArithmetic):

    # Constructor
    def __init__(self, real, imaginary):
        super().__init__(real, imaginary)

    # Conjugate of complex number
    def conjugate(self):
        return ComplexAdvanced(self._real, -self._imaginary)

    # Modulus of complex number
    def modulus(self):
        return math.sqrt((self._real ** 2) + (self._imaginary ** 2))

    # Destructor
    def __del__(self):
        print("ComplexAdvanced object destroyed")