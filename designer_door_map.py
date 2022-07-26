# Input Format:
#     A single line containing the space separated values of `n` and `m`.
#
# Output Format:
#     Output the design pattern.

a = input().split(" ")
n, m = int(a[0]), int(a[1])

for i in range(n):
    pat = ".|."
    if i < (n - 1) / 2:
        print((pat * (2 * i + 1)).center(m, "-"))
    elif i == (n - 1) / 2:
        print("WELCOME".center(m, "-"))
    else:
        print((pat * (2 * (n - 1 - i) + 1)).center(m, "-"))
