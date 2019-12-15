# 1) Создать декоратор с аргументами.
# Который будет вызывать функцию, определенное кол-во раз, будет выводить кол-во времени
# затраченного на выполнение данной функции и её название.

from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def cycle_for(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit
def generator_my(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

l1 = cycle_for(10)
l2 = generator_my(10)

print(type(l1), cycle_for.__name__, l1)
print(type(l2), generator_my.__name__, l2)

