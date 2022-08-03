# Input Format:
#     The first line contains the number of students who have subscribed to the English newspaper.
#     The second line contains the space separated list of student roll numbers who have subscribed
#     to the English newspaper.
#     The third line contains the number of students who have subscribed to the French newspaper.
#     The fourth line contains the space separated list of student roll numbers who have subscribed
#     to the French newspaper.
#
# Output Format:
#     Output the total number of students who are subscribed to the English newspaper only.

x, y = input(), set(input().split())
z, w = input(), set(input().split())

print(len(y.difference(w)))
