def minion_game(string):
    string = s
    vow = 'AEIOU'

    kevin = 0
    stuart = 0
    for x in range(len(s)):
        if s[x] in vow:
            kevin += (len(s) - x)
        else:
            stuart += (len(s) - x)

    if kevin > stuart:
        print("Kevin {}".format(kevin))
    elif kevin < stuart:
        print("Stuart {}".format(stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
