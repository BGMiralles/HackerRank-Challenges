# Given an integer, `n`, print the following values for each integer `i` from to `n`:
#     Decimal
#     Octal
#     Hexadecimal (capitalized)
#     Binary
#
# Prints:
#     The four values must be printed on a single line in the order specified above for each `i` from to `number`.
#     Each value should be space-padded to match the width of the binary value of and `number`
#     the values should be separated by a single space.
#
# Input Format:
#     A single integer denoting `n`.

def print_formatted(number):
    spaces = len(bin(n)[2:])
    for x in range(1, number + 1):
        s = str(x).rjust(spaces, ' ')
        o = str(oct(x)[2:]).rjust(spaces, ' ')
        h = str(hex(x)[2:]).upper().rjust(spaces, ' ')
        b = str(bin(x)[2:]).rjust(spaces, ' ')
        print(s, o, h, b)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)