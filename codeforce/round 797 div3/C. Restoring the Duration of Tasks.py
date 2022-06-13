import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))

    r = [0] * n
    r[0] = s[0]

    for i in range(1, n):
        r[i] = max(f[i-1], s[i])
    d = [fi - ri for fi, ri in zip(f, r)]
    print(*d)
