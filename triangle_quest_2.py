# Input Format:
#     A single line of input containing the integer `N`.
#
# Output Format:
#     Print the palindromic triangle of size `N` as explained above.

for i in range(1, int(input()) + 1):
    print(((10 ** i) // 9) ** 2)
