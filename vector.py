class Vector:
    def __init__(self, *v):
        self.v = v

    def __str__(self):
        return "{}".format(self.v)

    def __repr__(self):  # this is what is called in iPython
        return self.__str__()

    def __add__(self, other):
        return Vector(*[c1 + c2 for c1, c2 in zip(self.v, other.v)])

    def dot(self, other):
        return sum((c1 * c2 for c1, c2 in zip(self.v, other.v)))

    def scale(self, scalar):
        return Vector(*[scalar * i for i in self.v])

    def norm(self):
        return self.dot(self) ** 0.5

    def v_length(self):
        return len(self.v)
