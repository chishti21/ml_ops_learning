import math
from complex_number import ComplexNumber
from complex_arithmetic import ComplexArithmetic
from complex_advanced import ComplexAdvanced

if __name__ == "__main__":

    print("---- ComplexNumber Tests ----")
    c1 = ComplexNumber()
    c2 = ComplexNumber(3, 4)
    c3 = ComplexNumber.copy(c2)

    c1.display()
    c2.display()
    c3.display()

    print("\n---- ComplexArithmetic Tests ----")
    a1 = ComplexArithmetic(2, 3)
    a2 = ComplexArithmetic(4, -5)

    sum_result = a1.add(a2)
    product_result = a1.multiply(a2)

    print("Sum:")
    sum_result.display()

    print("Product:")
    product_result.display()

    print("\n---- ComplexAdvanced Tests ----")
    adv = ComplexAdvanced(3, 4)

    conjugate = adv.conjugate()
    modulus = adv.modulus()

    print("Original:")
    adv.display()

    print("Conjugate:")
    conjugate.display()

    print(f"Modulus: {modulus}")
