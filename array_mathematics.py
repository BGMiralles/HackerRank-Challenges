# Task:
#     You are given two integer arrays, `a` and `b` of dimensions NxM.
#     Your task is to perform the following operations:
#     Add (a + b)
#     Subtract (a - b)
#     Multiply (a * b)
#     Integer Division (a / b)
#     Mod (a % b)
#     Power (a ** b)
#
# Input Format:
#     The first line contains two space separated integers, `N` and `M`.
#     The next `N` lines contains `M` space separated integers of array `a`.
#     The following `N` lines contains `M` space separated integers of array `b`.
#
# Output Format:
#     Print the result of each operation in the given order under Task.

import numpy

n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(input().split())
a = numpy.array(a, int)

for _ in range(n):
    b.append(input().split())
b = numpy.array(b, int)

print(a + b, a - b, a * b, a // b, a % b, a ** b, sep="\n")
