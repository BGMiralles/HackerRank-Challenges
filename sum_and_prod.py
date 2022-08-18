# Task:
#     You are given a 2-D array with dimensions NxM.
#     Your task is to perform the sum tool over axis 0 and then find the product of that result.
#
# Input Format:
#     The first line of input contains space separated values of `n` and `m`.
#     The next `n` lines contains `m` space separated integers.
#
# Output Format:
#     Compute the sum along axis 0. Then, print the product of that sum.

import numpy

n, m = input().split()

arr = []
for _ in range(int(n)):
    arr.append(input().split())
arr = numpy.array(arr, int)

sum_arr = numpy.sum(arr, axis=0)
print(numpy.prod(sum_arr))
