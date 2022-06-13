import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

t = int(input())
while t:
    t -= 1

    n, m, k = map(int, input().split())
    a = list(input())
    b = list(input())
    a.sort(reverse=True)
    b.sort(reverse=True)

    c = []
    checker = True
    ka, kb = 0, 0
    while a and b:
        if a[-1] < b[-1]:
            checker = True
        else:
            checker = False

        if checker and ka == k: checker = False
        if not checker and kb == k: checker = True

        if checker:
            c.append(a.pop())
            ka += 1
            kb = 0
        else:
            c.append(b.pop())
            kb += 1
            ka = 0

    print(''.join(c))
