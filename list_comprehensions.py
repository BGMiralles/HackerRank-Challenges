# Input Format:
#
# Four integers x,y,z and n, each on a separate line.
#
# Constraints:
#
# Print the list in lexicographic increasing order.
#
# Sample Input:
#
# 1
# 1
# 1
# 2


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

coordinates = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                coordinates.append([i, j, k])

print(coordinates)