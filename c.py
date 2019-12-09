class A():

    def b(self):
        pass

class B(A):

    def b(self):
        print('Do something useful')
        super().b()
        print('Do something useful')


def square_root(number):
    return number ** 2


a = map(lambda number: number ** 2, range(100))
print(list(a))
