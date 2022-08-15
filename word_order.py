# Input Format:
#     The first line contains the integer, `n`.
#     The next `n` lines each contain a word.
#
# Output Format:
#     Output 2 lines.
#     On the first line, output the number of distinct words from the input.
#     On the second line, output the number of occurrences for each distinct word according to their
#     appearance in the input.

n = int(input())
total = {}

for x in range(n):
    st = input()
    if st in total:
        total[st] += 1
    else:
        total[st] = 1

print(len(total))
print(*total.values())
