import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())

    p = list(map(int, input().split()))
    setter = 1

    used = [False] * (n + 2)
    if n == 1:
        print(-1)
        continue

    q = [0] * n
    for i in range(n-1):
        while used[setter]:
            setter += 1

        if p[i] == setter:
            q[i] = setter + 1
        else:
            q[i] = setter

        used[q[i]] = True
    if setter == p[-1]:
        q[-1], q[-2] = p[-1], n
    else:
        q[-1] = n
    print(*q)


