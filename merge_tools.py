def merge_the_tools(s, k):
    lst = []
    new_lst = []
    for x in range(0, len(s), k):
        lst.append(s[x: (x + k)])
    for y in lst:
        for z in y:
            if z not in new_lst:
                new_lst.append(z)
        print("".join(new_lst))
        new_lst = []


if __name__ == '__main__':
    s, k = input(), int(input())
    merge_the_tools(s, k)
