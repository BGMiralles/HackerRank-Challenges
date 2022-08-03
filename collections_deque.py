from collections import deque

n = int(input())
d = deque()

for x in range(int(n)):
    commands = input().split()
    if commands[0] == "append":
        d.append(commands[1])
    elif commands[0] == "appendleft":
        d.appendleft(commands[1])
    elif commands[0] == "pop":
        d.pop()
    elif commands[0] == "popleft":
        d.popleft()

print(*d)
