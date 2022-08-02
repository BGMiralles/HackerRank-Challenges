# Task:
#     You have a non-empty set, and you have to execute `N` commands given in `N` lines.
#     The commands will be pop, remove and discard.
#
# Input Format:
#     The first line contains integer `n`, the number of elements in the set.
#     The second line contains `n` space separated elements of set. All of the elements are
#     non-negative integers, less than or equal to 9.
#     The third line contains integer `N`, the number of commands.
#     The next `N` lines contains either pop, remove and/or discard commands followed by their associated value.
#
# Output Format:
#     Print the sum of the elements of set on a single line.

n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for x in range(commands):
    todo = input().split()
    if todo[0] == "pop":
        s.pop()
    elif todo[0] == "remove":
        s.remove(int(todo[1]))
    elif todo[0] == "discard":
        s.discard(int(todo[1]))

print(sum(s))
