# A valid credit card from ABCD Bank has the following characteristics:
#     ► It must start with a , or .
#     ► It must contain exactly digits.
#     ► It must only consist of digits (-).
#     ► It may have digits in groups of , separated by one hyphen "-".
#     ► It must NOT use any other separator like ' ' , '_', etc.
#     ► It must NOT have or more consecutive repeated digits. 

# Input Format:
#     The first line of input contains an integer `N`.
#     The next `N` lines contain credit card numbers. 

# Output Format:
#     Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.
    
import re


for _ in range(int(input())):
    s = input()
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")
