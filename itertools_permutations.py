# Task:
#     You are given a string `S`.
#     Your task is to print all possible permutations of size `k` of the string in lexicographic sorted order.
#
# Input Format:
#     A single line containing the space separated string `S` and the integer value .
#
# Output Format:
#     Print the permutations of the string `S` on separate lines.

from itertools import permutations

st, num = input().split(" ")

permu = list(permutations(st, int(num)))
permu.sort()

for x in permu:
    print("".join(x))
