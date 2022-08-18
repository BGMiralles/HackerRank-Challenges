# Input Format:
#     The first line contains the space separated elements of array `a`.
#     The second line contains the space separated elements of array `b`.
#
# Output Format
#     First, print the inner product.
#     Second, print the outer product.

import numpy

a = input().split()
a = numpy.array(a, int)

b = input().split()
b = numpy.array(b, int)

print(numpy.inner(a, b), numpy.outer(a, b), sep='\n')
