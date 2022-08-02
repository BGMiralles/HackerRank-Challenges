# Input Format:
#     The first line contains an integer `N`, the total number of country stamps.
#     The next `N` lines contains the name of the country where the stamp is from.
#
# Output Format:
#     Output the total number of distinct country stamps on a single line.

n = input()
s = set()

for x in range(int(n)):
    s.add(input())

print(len(s))