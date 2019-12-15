# Создать класс комплексного числа и реализовать для него арифметические операции.

class ComplexMy:

    def __init__(self, x, y):
        self.x = complex(x, y)
        self.y = complex(x, y)
        print('Working...')

    def __add__(self, other):
        return (self.x + other.x)

    def __truediv__(self, other):
        return (self.x / other.x)

    def __mul__(self, other):
        return (self.x * other.x)

    def __sub__(self, other):
        return (self.x - other.x)


my_fun = ComplexMy(1, 2)
my_fun2 = ComplexMy(1, 2)

x1 = my_fun + my_fun2
x2 = my_fun * my_fun2
x3 = my_fun - my_fun2
x4 = my_fun / my_fun2

print(x1, x1.real, x1.imag)
print(x2, x2.real, x2.imag)
print(x3, x3.real, x3.imag)
print(x4, x4.real, x4.imag)