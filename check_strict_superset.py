# Input Format:
#     The first line contains the space separated elements of set `A`.
#     The second line contains integer `n`, the number of other sets.
#     The next `n` lines contains the space separated elements of the other sets.
#
# Output Format:
#     Print True if set `A` is a strict superset of all other `n` sets. Otherwise, print False.

a = set(input().split())
n = input()
y = []

for _ in range(int(n)):
    y.append(a.issuperset(set(input().split())))

print(all(y))
