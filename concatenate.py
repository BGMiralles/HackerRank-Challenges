# Task:
#     You are given two integer arrays of size NxP and MxP(N & M are rows, and is the column).
#     Your task is to concatenate the arrays along axis 0.
#
# Input Format:
#     The first line contains space separated integers `N`, `M` and `P`.
#     The next `N` lines contains the space separated elements of the `P` columns.
#     After that, the next `M` lines contains the space separated elements of the `P` columns.
#
# Output Format
#     Print the concatenated array of size (N + M) x P.

import numpy


n, m, p = map(int, input().split())
arr1 = numpy.array([input().split() for _ in range(n)], int)
arr2 = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((arr1, arr2), axis=0))
