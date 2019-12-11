
def sum_func(my_arg1, *args, name='MyName',**kwargs):

    result = 0
    print(kwargs)
    print(*kwargs.values())
    print(my_arg1)
    print(name)
    for i in args:
        result += i
    return result


a = [1, 2, 3, 4]

b = {'1':'2',
     '3':'4'}
sum_func(*a, **b)
print(sum_func(*a, 1, 2, 3, 4))


