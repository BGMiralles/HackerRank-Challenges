a, b = input(), input().split()
c, d = input(), input().split()

x = set(b)
y = set(d)

z = x.difference(y)
w = y.difference(x)

sym_dif = z.union(w)
print("\n".join(sorted(sym_dif, key=int)))
