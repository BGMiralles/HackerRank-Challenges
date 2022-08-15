# Input Format:
#     The first line contains `N`, the number of code lines.
#     The next `N` lines contains CSS Codes.
#
# Output Format:
#     Output the color codes with '#' symbols on separate lines.

import re

patt = re.compile(r'(?<!^)(#(?:[0-9a-fA-F]{3}){1,2})')

for _ in range(int(input())):
    line = input()
    match = patt.findall(line)
    if match:
        print(*match, sep='\n')
