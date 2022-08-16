# A valid UID must follow the rules below:
#     It must contain at least 2 uppercase English alphabet characters.
#     It must contain at least 2 digits (0-9).
#     It should only contain alphanumeric characters (a-z, A-Z & 0-9).
#     No character should repeat.
#     There must be exactly 10 characters in a valid UID.
#
# Input Format:
#     The first line contains an integer `T`, the number of test cases.
#     The next `T` lines contains an employee's UID.
#
# Output Format:
#     For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines.
#     Do not print the quotation marks.

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert re.search(r'[a-zA-Z0-9]', u)
        assert not re.search(r'(\w)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
