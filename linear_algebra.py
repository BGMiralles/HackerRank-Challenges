# Task:
#     You are given a square matrix `a` with dimensions NxN. Your task is to find the determinant.
#     Note: Round the answer to 2 places after the decimal.
#
# Input Format:
#     The first line contains the integer `N`.
#     The next `N` lines contains the `N` space separated elements of array `a`.
#
# Output Format:
#     Print the determinant of `a`.

import numpy

n = input()

a = []
for _ in range(int(n)):
    a.append(input().split())
a = numpy.array(a, float)

print(numpy.round(numpy.linalg.det(a), decimals=2))
