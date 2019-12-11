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


a = map(lambda number: number + 1, range(5))
print(list(a))
