class Complex:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.i = 'i'

    def __add__(self, other):
        add_a = self.a + other.a
        add_b = self.b + other.b
        if add_a != 0 and add_b != 0:
            if add_b > 0:
                if add_b == 1:
                    return str(add_a) + ' + ' + self.i
                return str(add_a) + ' + ' + str(add_b) + self.i
            elif add_b < 0:
                if add_b == -1:
                    return str(add_a) + ' - ' + self.i
                add_b *= -1
                return str(add_a) + ' - ' + str(add_b) + self.i
        elif add_a == 0 and add_b == 0:
            return 0
        else:
            if add_a == 0:
                if add_b == 1:
                    return self.i
                return str(add_b) + self.i
            elif add_b == 0:
                return add_a

    def __mul__(self, other):
        mul1 = self.a * other.a - self.b * other.b
        mul2 = self.a * other.b + self.b * other.a
        if mul1 != 0 and mul2 != 0:
            if mul2 > 0:
                if mul2 == 1:
                    return str(mul1) + ' + ' + self.i
                return str(mul1) + ' + ' + str(mul2) + self.i
            elif mul2 < 0:
                if mul2 == -1:
                    return str(mul1) + ' - ' + self.i
                mul2 *= -1
                return str(mul1) + ' - ' + str(mul2) + self.i
        elif mul1 == 0 and mul2 == 0:
            return 0
        else:
            if mul1 == 0:
                if mul2 == 1:
                    return self.i
                return str(mul2) + self.i
            elif mul2 == 0:
                return mul1


a = Complex(1, 3)
b = Complex(4, -5)
c = Complex(3, 5)
d = Complex(-4, 6)
e = Complex(-4, 5)
f = Complex(2, 3)
g = Complex(-1, 1)
h = Complex(3, 6)
print(a + b)
print(a + c)
print(b + c)
print(b + d)
print(b + e)
print(b + h)
print(f * g)
print(d * a)
print(h * c)
print(g * a)
