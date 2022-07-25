# Input Format:
#
# The first line contains an integer, `n1, denoting the number of elements in the tuple.
# The second line contains `n` space-separated integers describing the elements in tuple `t`.
#
# Output Format:
#
# Print the result of hash(t).

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list = tuple(integer_list)
    print(hash(integer_list))
