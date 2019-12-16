#
# a = "test"
# print(type(str))
# print(type(a))
#
def my_func():
     pass

print(type(MyClass))

a = type('MyClass', (), {'attr1': 1,
                         'attr2': 2,
                         'func_1': my_func})

print(a)
print(dir(a))
