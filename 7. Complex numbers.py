class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if int(self.b + other.b) < 0:
            minus = ''
        else:
            minus = '+'
        return f'{self.a + other.a} {minus}{self.b + other.b}i'

    def __mul__(self, other):
        if int(self.a * other.b + self.b * other.a) < 0:
            minus = ''
        else:
            minus = '+'
        return f'{self.a * other.a - self.b * other.b} {minus}{self.a * other.b + self.b * other.a}i'


complex_1 = ComplexNum(3, 1)
complex_2 = ComplexNum(2, -3)
complex_3 = ComplexNum(5, -6)
complex_4 = ComplexNum(-3, 2)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
print(5 * '*')
print(complex_3 + complex_4)
print(complex_3 * complex_4)
