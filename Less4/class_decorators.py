class Shop:

    _total_sales = 0

    def __init__(self, name, sales):
        self._name = name
        self._sales = sales
        Shop._total_sales +=sales

    @classmethod
    def get_total_sales(cls):
        return cls._total_sales

    @staticmethod
    def get_total_static_sales():
        return Shop._total_sales

    def __call__(self, *args, **kwargs):
        print(f'HI I am {self.__class__.__name__}')

Shop.get_total_sales()
shop_obj = Shop('ATB', 4000)
shop_obj()


class Decorator:

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        rint(f'HI I am {self._func_.__name__}')
        self._func()

@Decorator
def func():
    pass