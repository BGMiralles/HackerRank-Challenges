n = input()
rooms = input().split()

rooms.sort()
print(rooms)
cap_room = set(rooms[0::2]).symmetric_difference(set(rooms[1::2]))
print(cap_room.pop())
