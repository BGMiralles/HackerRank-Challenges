# Input Format:
#     A single line containing integer, `N`.
#
# Output Format:
#     Print `N - 1` lines as explained above.

for i in range(1, int(input())):
    print((10 ** i // 9) * i)
