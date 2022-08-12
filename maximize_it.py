# You are given a function f(X) = X ** 2. You are also given `K` lists. The list consists of `N` elements.
# You have to pick one element from each list so that the value from the equation below is maximized:
# S = (F(X) + f(X2) + ... + f(Xk)) % M
#
# Input Format:
#     The first line contains 2 space separated integers `K` and `M`.
#     The next `K` lines each contains an integer `N`, denoting the number of elements in the `i` list,
#     followed by `N` space separated integers denoting the elements in the list.
#
# Output Format:
#     Output a single integer denoting the value `Smax`.

from itertools import product


def square(n):
    return int(n) ** 2


k, m = input().split()

lis = []
for i in range(int(k)):
    lis.append(list(map(square, input().split()[1:])))

max = 0
for x in product(*lis):
    s = sum(x) % int(m)
    if s > max:
        max = s

print(max)
