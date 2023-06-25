from utils.complex_number import ComplexNumber


def test_repr_and_str():
    complex_number = ComplexNumber(1, 1)
    assert str(complex_number) == "1 + 1i"
    assert repr(complex_number) == "1 + 1i"

    complex_number = ComplexNumber(1.1, 2.2)
    assert str(complex_number) == "1.1 + 2.2i"
    assert repr(complex_number) == "1.1 + 2.2i"

    complex_number = ComplexNumber(-1, -1)
    assert str(complex_number) == "-1 - 1i"
    assert repr(complex_number) == "-1 - 1i"


def test_mul():
    complex_number_1 = ComplexNumber(3, 3)
    complex_number_2 = ComplexNumber(4, -4)
    complex_number_3 = complex_number_1 * complex_number_2

    assert complex_number_3.real == 24
    assert complex_number_3.imag == 0

    complex_number_1 = ComplexNumber(3, 3)
    complex_number_2 = ComplexNumber(4, 5)
    complex_number_3 = complex_number_1 * complex_number_2

    assert complex_number_3.real == -3
    assert complex_number_3.imag == 27


def test_add():
    complex_number_1 = ComplexNumber(3, 3)
    complex_number_2 = ComplexNumber(4, -4)
    complex_number_3 = complex_number_1 + complex_number_2

    assert complex_number_3.real == 7
    assert complex_number_3.imag == -1
