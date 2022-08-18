# Task:
#     You are given a 2-D array of size NxM.
#     Your task is to find:
#     The mean along axis 1
#     The var along axis 0
#     The std along axis None
#
# Input Format:
#     The first line contains the space separated values of `N` and `M`.
#     The next `N` lines contains `M` space separated integers.
#
# Output Format:
#     First, print the mean.
#     Second, print the var.
#     Third, print the std.

import numpy

n, m = input().split()
x = []

for _ in range(int(n)):
    x.append(input().split())
x = numpy.array(x, int)

print(numpy.mean(x, axis=1), numpy.var(x, axis=0), numpy.std(x), sep="\n")
