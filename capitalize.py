def solve(s):
    return ' '.join(word.capitalize() for word in s)


s = input().split(' ')
print(solve(s))
