import re

n = int(input())

for _ in range(n):
    pat = re.compile(r'(?<= )(&&)(?= )')
    patt = re.compile(r'(?<= )(\|\|)(?= )')
    print(patt.sub('or', pat.sub('and', input())))
