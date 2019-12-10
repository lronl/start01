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
    quantity: int
    store = 'shop'

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        print("Store ready")

my_shop = Shop('Auchan', 2)
my_sold = Shop(1, 0)

i = 0
while i < 10:
    print('Auchan Sell:', i, 'Goods')
    i = i + 1
    time.sleep(0.4)

print(my_shop.name, 'Total Sell :', my_sold.quantity + i)

# Создать класс точки, реализовать конструктор который
# инициализирует 3 координаты (Class): Определенный программистом тип данных.x, y, z). Реалзиовать методы для ). Реалзиовать методы для
# получения и изменения каждой из координат. Перегрузить для этого
# класса методы сложения, вычитания, деления умножения.
# Перегрузить один любой унарный метод.
# Ожидаемый результат: умножаю точку с координатами 1,2,3 на
# другую точку с такими же координатами, получаю результат 1, 4, 9.