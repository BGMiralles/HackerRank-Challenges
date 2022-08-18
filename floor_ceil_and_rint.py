# Task:
#     You are given a 1-D array, `a`. Your task is to print the floor, ceil and rint of all the elements of `a`.
#
# Note:
#     In order to get the correct output format, add the line numpy.set_printoptions(legacy='1.13')
#     below the numpy import.
#
# Input Format:
#     A single line of input containing the space separated elements of array `a`.
#
# Output Format:
#     On the first line, print the floor of `a`.
#     On the second line, print the of ceil `a`.
#     On the third line, print the of rint `a`.

import numpy

numpy.set_printoptions(legacy='1.13')

a = list(map(float, input().split()))
a = numpy.array(a)

print(numpy.floor(a), numpy.ceil(a), numpy.rint(a), sep="\n")
