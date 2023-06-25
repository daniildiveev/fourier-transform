from typing import Union


class ComplexNumber:
    def __init__(self, real: Union[float, int], imag: Union[float, int]):
        self.real = real
        self.imag = imag

    def __str__(self) -> str:
        if self.imag > 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    def __repr__(self) -> str:
        return self.__str__()

    def __mul__(self, other) -> 'ComplexNumber':
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.imag * other.real + other.imag * self.real)

    def __add__(self, other) -> 'ComplexNumber':
        return ComplexNumber(self.real + other.real, self.imag + other.imag)