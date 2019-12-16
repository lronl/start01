class Dot:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_x(self, value):
        self._x = value

    def get_x(self):
        return self._x

    x = property(get_x, set_x)

    def set_y(self, value):
        self._y = value

    def get_y(self):
        return self._y

    # @property
    # def x(self):
    #     return self._x
    #
    # @x.setter
    # def x(self, value):
    #     if value < 0:
    #         print('Values must be positive')
    #         self.x = 0
    #     self._x = value
    #     return None

obj = Dot(1, 2)
print(obj.x)

obj.x = -20
print(obj.x)
