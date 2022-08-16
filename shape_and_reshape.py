# Task:
#     You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.
#
# Input Format:
#     A single line of input containing 9 space separated integers.
#
# Output Format:
#     Print the 3X3 NumPy array.

import numpy

change_array = numpy.array(input().split(), int)
change_array.shape = (3, 3)
print(change_array)
