from matrix import Matrix

from vector import Vector
from functools import reduce
from collections import defaultdict


# 1 cry
# 2 goto 1
# read in the matrix.txt
# filter the 4x2 and 2x4 matrices into
# different lists

# add any 2 compatible matrices
# multiply any 2 compatible matrices
# scale any matrix
# create a list of 5 3x3 matrices of random values
# and add them together

# multiply a matrix times a vector

t1 = (1, 2)
t2 = (4, 5)
t3 = (7, 8)

v1 = Vector(*t1)
v2 = Vector(*t2)
v3 = Vector(*t3)

v_main = [v1, v2, v3]


m1 = Matrix(*v_main)
# print(m1)
# print(m1.row, m1.col)


m2 = Matrix.random(3, 4)
# print(m2)
# print(m2.row, m2.col)

m3 = m1.scale_it(3)
# print(m3)
# print(m3.row, m3.col)

m4 = m1.add_them(m1)
# print(m1)
# print(m4)
# print(m4.row, m4.col)

# m5 = m1.mult_them(m1)


with open('matrix.txt') as f:
    matrices = []
    vectors = []
    for line in f:
        line = line.strip()
        if not line:
            matrix = Matrix(*vectors)
            matrices.append(matrix)
            vectors = []
        else:
            vector = Vector(*map(float, line.split(' ')))
            vectors.append(vector)
    matrix = Matrix(*vectors)
    matrices.append(matrix)

# print all the matrices
for i, m in enumerate(matrices):
    print(i, 'rows: ', m.row, '\n', 'columns: ', m.col, '\n', m, '\n', '-' * 25)

# filter matrices
d = defaultdict(list)
[d[m.shape].append(m) for m in matrices]
print('filtered:', d)

# create 5 3x3 matrices and add together
zero = Vector(0, 0, 0)
final = reduce(lambda acc, mat: acc.add_them(mat),
               [Matrix.random(3, 3) for i in range(5)],
               Matrix(zero, zero, zero))
print('final: ', '\n', final)

# find the dot product of two matrices
dotted = d[(2, 4)][0].dot(d[(4, 2)][0])
print('dotted: ', '\n', dotted)
