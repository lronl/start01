class List(list):

    def __add__(self, other):
        if isinstance(other, list):
            return super(List, self).__add__(other)
        else:
            return self + [other]

    def __radd__(self, other):
        if isinstance(other, list):
            return other.__add__(self)
        else:
            return [other].__add__(self)