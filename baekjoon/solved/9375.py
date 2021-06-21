import sys
input = sys.stdin.readline

TC = int(input())
while TC:
    TC -= 1
    n = int(input())
    dic = {}

    for _ in range(n):
        item, key = input().split()
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 2

    ret = 1
    for n in dic.values():
        ret *= n
    print(ret - 1)