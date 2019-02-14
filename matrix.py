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
        self.shape = (len(v), v[0].v_length())

    # def __str__(self):
    #     return "Matrix {}. \n".format(self.matrix)

    def __repr__(self):  # this is what is called in iPython
        return self.__str__()

    def scale_it(self, scalar):
        return Matrix(*[v.scale(scalar) for v in self.matrix])

    def add_them(self, other):
        if (self.row != other.row) or (self.col != other.col):
            return "The matrices could not be added because they do not have the same dimensions."
        return Matrix(*[row + orow for row, orow in
                        zip(self.matrix, other.matrix)])

    # def mult_them(self, other):
    #     m = self.row
    #     n = self.col
    #     for i in range(m):
    #         entry = 0
    #         entry = self.matrix[i]
    #         print(entry)

    # @staticmethod
    def random(m, n):  # rewrite using for and range
        vecs = []
        for i in range(m):
            v = []
            for j in range(n):
                v.append(r.random())
            vecs.append(Vector(*v))
        return Matrix(*vecs)

    # Chyld's
    # @staticmethod
    # def random(rows, cols):
    #     randrows = [[r.random() for c in range(cols)] for r in range(rows)]
    #     return Matrix(*[Vector(*row) for row in randrows])

    def __str__(self):
        n1 = '\n'
        return f"[{n1.join([str(v) for v in self.matrix])}]"

    def dot(self, other):
        if (self.row != other.col) or (self.col != other.row):
            return
        column_vectors = [Vector(*col) for col in zip(*[m.v for m in other.matrix])]
        transposed = Matrix(*column_vectors)
        vectors = []
        for row in self.matrix:
            nums = []
            for col in transposed.matrix:
                scalar = row.dot(col)
                nums.append(scalar)
            vector = Vector(*nums)
            vectors.append(vector)
        return Matrix(*vectors)
