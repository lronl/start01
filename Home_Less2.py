# 1) Создать класс автомобиля. Описать общие аттрибуты. Создать
# классы легкового автомобиля и грузового. Описать в основном
# классе базовые аттрибуты для автомобилей. Будет плюсом если в
# классах наследниках переопределите методы базового класса.
class Car:
    vehicle = 'car'

    def __init__(self, num_of_doors, num_of_wheels, brand, max_weight, color):
        self.num_of_doors = num_of_doors
        self.num_of_whells = num_of_wheels
        self.brand = brand
        self.max_weight = max_weight
        self.color = color

CarPassenger = Car(4, 4, "Lada", 300, "Black")
Truck = Car(2, 6, "Niva", 700, "Black")

print('Passenger:', 'It is a', CarPassenger.vehicle + ',', 'the car has', CarPassenger.num_of_doors, 'doors,', CarPassenger.num_of_whells, 'whells,', 'it is a', CarPassenger.brand, 'her maximum lifting weight', CarPassenger.max_weight, 'and the color is', CarPassenger.color)
print('Truck:', 'It is a', Truck.vehicle + ',', 'the car has', Truck.num_of_doors, 'doors,', Truck.num_of_whells, 'whells,', 'it is a', Truck.brand, 'her maximum lifting weight', Truck.max_weight, 'and the color is', Truck.color)

# 2) Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.

import time

class Shop:

    total_sell = 0

    def __init__(self, name, sold):
        self.name = name
        self.sold = sold
        print('\n(Продажа в {0})'.format(self.name))
        Shop.total_sell += 1

    def Store_sold(self):
        print('Приветствую! Клиент совершил покупку в магазине {0}.'.format(self.name))
        time.sleep(0.4)

    def howMany():
        print('У нас {0:d} Продажи.'.format(Shop.total_sell))
        time.sleep(0.4)

    howMany = staticmethod(howMany)

obj1 = Shop('Auchan', 0)
obj1.Store_sold()
Shop.howMany()

obj2 = Shop('Silpo', 0)
obj2.Store_sold()
Shop.howMany()

print('\nВ', obj1.name, 'и', obj2.name, 'были продажи!'), Shop.howMany()

# Создать класс точки, реализовать конструктор который
# инициализирует 3 координаты (Class): Определенный программистом тип данных.x, y, z). Реалзиовать методы для ). Реалзиовать методы для
# получения и изменения каждой из координат. Перегрузить для этого
# класса методы сложения, вычитания, деления умножения.
# Перегрузить один любой унарный метод.
# Ожидаемый результат: умножаю точку с координатами 1,2,3 на
# другую точку с такими же координатами, получаю результат 1, 4, 9.

class Point:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        print('Working...')

    def set_x(self, new_x):
        self._x = new_x

    def get_x(self):
        return self._x

    def set_y(self, new_y):
        self._y = new_y

    def get_y(self):
        return self._y

    def set_z(self, new_z):
        self._z = new_z

    def get_z(self):
        return self._z

    def __add__(self, other):
        return (self.get_x() + other.get_x(),
                self.get_y() + other.get_y(),
                self.get_z() + other.get_z())

    def __truediv__(self, other):
        return (self.get_x() / other.get_x(),
                self.get_y() / other.get_y(),
                self.get_z() / other.get_z())

    def __mul__(self, other):
        return (self.get_x() * other.get_x(),
                self.get_y() * other.get_y(),
                self.get_z() * other.get_z())

    def __sub__(self, other):
        return (self.get_x() - other.get_x(),
                self.get_y() - other.get_y(),
                self.get_z() - other.get_z())


my_fun = Point(1, 2, 3)
my_fun2 = Point(1, 2, 3)

print(my_fun + my_fun2)
print(my_fun * my_fun2)
print(my_fun - my_fun2)
print(my_fun / my_fun2)