# 1) Создать декоратор с аргументами.
# Который будет вызывать функцию, определенное кол-во раз, будет выводить кол-во времени
# затраченного на выполнение данной функции и её название.

from datetime import datetime


class date_time:

    total_range = 0


def timeit(func):
    def res(arg1, arg2):
        start = datetime.now()
        for i in range(arg1, arg2):
            print(i)
            date_time.total_range += 1
        func(arg1, arg2)
        print(datetime.now() - start)
    return res


@timeit
def res_call(start, end):
    print("Диапазоп от:", start, end)

res_call(1, 100)
print(date_time.total_range)

