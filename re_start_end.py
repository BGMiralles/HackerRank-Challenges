# Task:
#     You are given a string `S`.
#     Your task is to find the indices of the start and end of string `k` in `S`.
#
# Input Format:
#     The first line contains the string `S`.
#     The second line contains the string `k`.
#
# Output Format:
#     Print the tuple in this format: (start _index, end _index).
#     If no match is found, print (-1, -1).

import re

S = input()
k = input()
m = re.search(k, S)
pattern = re.compile(k)

if not m: print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(), m.end() - 1))
    m = pattern.search(S, m.start() + 1)
