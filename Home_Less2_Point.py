class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print('Working...')

    def __add__(self, other):
        return (self.x + other.x,
                self.y + other.y,
                self.z + other.z)

    def __truediv__(self, other):
        return (self.x / other.x,
                self.y / other.y,
                self.z / other.z)

    def __mul__(self, other):
        return (self.x * other.x,
                self.y * other.y,
                self.z * other.z)

    def __sub__(self, other):
        return (self.x - other.x,
                self.y - other.y,
                self.z - other.z)


my_fun = Point(1, 2, 3)
my_fun2 = Point(1, 2, 3)

print(my_fun + my_fun2)
print(my_fun * my_fun2)
print(my_fun - my_fun2)
print(my_fun / my_fun2)