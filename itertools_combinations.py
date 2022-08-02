# Task:
#     You are given a string `S`.
#     Your task is to print all possible combinations, up to size `k`, of the string in lexicographic
#     sorted order.
#
# Input Format:
#     A single line containing the string `S` and integer value `k` separated by a space.

from itertools import combinations

s, n = input().split()

for x in range(1, int(n) + 1):
    for y in combinations(sorted(s), x):
        print(''.join(y))
