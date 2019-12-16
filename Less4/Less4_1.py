class FromMeta:
    def hello(self):
        print('Hello')

class UpperCaseMetaclass(type):

    def __new__(cls, name, base, attrs):
        # print(name, base, attrs)
        for i in range(5):
            # new_base = FromMeta
            base = (FromMeta,)
            attrs.update({'var_' + str(i): i})
        return super().__new__(cls, name, base, attrs)


class Inhe():
    pass

class MyClass(Inhe, metaclass=UpperCaseMetaclass):

    _attribute_of_class = 'Attr'

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(dir(MyClass))
print(MyClass.__base__)
MyClass(1, 2).hello()


