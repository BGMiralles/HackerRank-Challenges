# Input Format:
#     The first line contains the integer `n`.
#     The next `n` lines contains `n` space separated integers of array `a`.
#     The following `n` lines contains `n` space separated integers of array `b`.
#
# Output Format:
#     Print the matrix multiplication of `a` and `b`.

import numpy

n = input()

a = []
for _ in range(int(n)):
    a.append(input().split())
a = numpy.array(a, int)

b = []
for _ in range(int(n)):
    b.append(input().split())
b = numpy.array(b, int)

print(numpy.dot(a, b))
