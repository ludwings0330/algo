import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = [bi - ai for bi, ai in zip(b, a)]
    k = max([abs(ci) for ci in c])
    a = [max(0, ai - k) for ai in a]
    if a == b:
        print('YES')
    else:
        print('NO')