from itertools import product

x = map(int, input().split())
y = map(int, input().split())

print(*product(x, y))