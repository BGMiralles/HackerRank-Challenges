trash = input()

check = ([int(x) for x in input().split()])
fset = set([int(x) for x in input().split()])
sset = set([int(x) for x in input().split()])

hap = 0
for x in check:
    if x in fset:
        hap += 1
    if x in sset:
        hap -= 1

print(hap)
