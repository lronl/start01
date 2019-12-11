class Vehicle:

    Vehicle_type = 'Car'

    def __init__(self, num_of_doors, num_of_wheels, brand):
        self._num_of_doors = num_of_doors
        self._num_of_whells = num_of_wheels
        self._brand = brand

    def get_brand(self):
        return self._brand

    def move(self):
        print('Moving')

class Car(Vehicle):

    def __init__(self, num_of_doors, num_of_wheels, brand, max_weight):
        self.num_of_doors = num_of_doors
        self.num_of_whells = num_of_wheels
        self.brand = brand
        self.max_weight = max_weight

    def __init__(self, num_of_doors, num_of_wheels, brand, max_weight):
        self.max_weight = max_weight
        super().__init__(num_of_doors, num_of_wheels, brand)
        self._engine = 'V-8'
    def get_engine(self):
        return self._engine

    def set_engine(self, value):
        if type(value) != str:
           raise ValidationError('Wrong type')
        self._engine = value

    def trasport_smth(self, weight, thing):
        print(f'transporting {thing}. Max weight is {weight}')

    def _change_oil(self):
        print('Changing_oil')
    def move(self):
        print('Moving fast')

    def __str__(self):
        return self._brand

car = Vehicle(4, 4, 'BMW')
#car.move()
#print(car.num_of_whells)
#print(car.num_of_doors)
#print(car.brand)
#print(car.Vehicle_type)
#car.Vehicle_type = 'Truck'
#print(car.Vehicle_type)

#car.new_varible = 100
#print(car.new_varible)


car1 = Car(4, 4, 'mercedess', 400)
car1.move()
car1.trasport_smth(200, "Animals")
car1.set_engine('V-8')
print(car1.get_engine())

print(dir(Car.__dict__))
print(car1.__dict__)

print(car1)




