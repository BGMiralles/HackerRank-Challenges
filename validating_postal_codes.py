# A valid postal code `P` have to fullfil both below requirements:
#     `P` must be a number in the range from 100000 to 999999 inclusive.
#     `P` must not contain more than one alternating repetitive digit pair.
#
# Input Format:
#     Locked stub code in the editor reads a single string denoting `P` from stdin and uses provided expression
#     and your regular expressions to validate if `P` is a valid postal code.
#
# Output Format:
#     You are not responsible for printing anything to stdout. Locked stub code in the editor does that.

import re

regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"

P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
