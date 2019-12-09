class Cat:

    def __init__(self, name):
        self._name = name

    def meow(self):
        print('Meow!')

    def say_my_name(self):
        print(f'My name is {self._name}')

    def __add__(obj1, obj2):
        return Cat(
            obj1._name + obj2._name
        )

    def __truediv__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __sub__(self, other):
        pass

cat1 = Cat('1')
cat2 = Cat('2')

cat3 = cat1 + cat2 #=> cat1.__add__(cat2)
cat3 = Cat(cat1._name + cat2._name)
cat3.say_my_name()
