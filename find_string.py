# Input Format:
#     The first line of input contains the original string. The next line contains the substring.
#
# Output Format:
#     Output the integer number indicating the total number of occurrences of the substring in the original string.

def count_substring(string, sub_string):
    r = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            r += 1
    return r


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
