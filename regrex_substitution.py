# Input Format:
#     The first line contains the integer, `N`.
#     The next `N` lines each contain a line of the text.

# Output Format:
#     Output the modified text.
    
import re

n = int(input())

for _ in range(n):
    pat = re.compile(r'(?<= )(&&)(?= )')
    patt = re.compile(r'(?<= )(\|\|)(?= )')
    print(patt.sub('or', pat.sub('and', input())))
