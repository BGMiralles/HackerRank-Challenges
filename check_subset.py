# Input Format:
#     The first line will contain the number of test cases, `T`.
#     The first line of each test case contains the number of elements in set `A`.
#     The second line of each test case contains the space separated elements of set `A`.
#     The third line of each test case contains the number of elements in set `B`.
#     The fourth line of each test case contains the space separated elements of set `B`.
#
# Output Format:
#     Output True or False for each test case on separate lines.

n = input()

for x in range(int(n)):
    _, y = input(), set(input().split())
    _, z = input(), set(input().split())
    print(y.issubset(z))
