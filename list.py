# Input Format:
#
# The first line contains an integer,`n`, denoting the number of commands.
# Each line `i` of the `n` subsequent lines contains one of the commands described above.
#
# Constraints:
#
# The elements added to the list must be integers.
#
# Output Format:
#
# For each command of type print, print the list on a new line.

if __name__ == '__main__':
    N = int(input())
    output = list()
    for _ in range(N):
        line = input().split(" ")
        if line[0] == "insert":
            output.insert(int(line[1]), int(line[2]))
        if line[0] == "print":
            print(output)
        if line[0] == "remove":
            output.remove(int(line[1]))
        if line[0] == "append":
            output.append(int(line[1]))
        if line[0] == "sort":
            output.sort()
        if line[0] == "pop":
            output.pop()
        if line[0] == "reverse":
            output.reverse()
