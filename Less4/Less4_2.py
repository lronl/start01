from abc import ABC, abstractmethod

class Vehicle(ABC):

    attr = 1

    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def beep(self):
        # print('Default beep')
        pass

class Car(Vehicle):

    def move(self):
        print('Moving')

    def beep(self):
        print('Beep')
        print('Car Beep')

Car().move()
Car().beep()

print(dir(Vehicle))

class MyABC:

    def my_method(self):
        raise NotImplemented

class MyClass(MyABC):
    pass

