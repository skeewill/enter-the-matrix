# create a matrix any dimension --> DONE
# scale matrix --> DONE
# create a random mxn matrix with values between 0 and 1 --> DONE
# add 2 matrices --> DONE
# multiply 2 matrices

from vector import Vector
import random as r


class Matrix:
    def __init__(self, *v):
        self.row = len(v)
        self.col = v[0].v_length()
        self.matrix = list(v)

    def __str__(self):
        return "Matrix {}. \n".format(self.matrix)

    def __repr__(self):  # this is what is called in iPython
        return self.__str__()

    def scale_it(self, scalar):
        return Matrix(*[v.scale(scalar) for v in self.matrix])

    def add_them(self, other):
        return Matrix(*[row + orow for row, orow in
                        zip(self.matrix, other.matrix)])

    def mult_them(self, other):
        m = self.row
        n = self.col
        for i in range(m):
            entry = 0
            entry = self.matrix[i]
            print(entry)

    @staticmethod
    def random(m, n):  # rewrite using for and range
        vecs = []
        for i in range(m):
            v = []
            for j in range(n):
                v.append(r.random())
            vecs.append(Vector(*v))
        return Matrix(*vecs)
