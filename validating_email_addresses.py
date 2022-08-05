# Input Format:
#     The first line contains a single integer, `n`, denoting the number of email address.
#     Each line `i` of the `n` subsequent lines contains a name and an email address as two space-separated values
#
# Output Format:
#     Print the space-separated name and email address pairs containing valid email addresses only.
#     Each pair must be printed on a new line

import re

n = int(input())

for _ in range(n):
    x, y = input().split(' ')
    z = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if z:
        print(x, y)
