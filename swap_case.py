# Function Description:
#
#   Complete the swap_case function in the editor below.
#
# swap_case has the following parameters:
#
#   string s: the string to modify
#
# Returns:
#
#   string: the modified string
#
# Input Format:
#
#   A single line containing a string.

def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
