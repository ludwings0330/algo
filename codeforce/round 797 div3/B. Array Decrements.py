import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_diff = max([abs(bi - ai) for bi, ai in zip(b, a)])
    a = [max(0, ai - max_diff) for ai in a]
    if a == b:
        print('YES')
    else:
        print('NO')