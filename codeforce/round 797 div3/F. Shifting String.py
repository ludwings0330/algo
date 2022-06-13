import sys
input = lambda: sys.stdin.readline().rstrip()


def gcd(A, B):
    if B == 0:
        return A
    return gcd(B, A%B)


def min_oper(s):
    for i in range(1, len(s) + 1):
        if s == s[i:] + s[:i]:
            return i


t = int(input())
while t:
    t -= 1
    n = int(input())
    s = list(input())
    p = [int(x) - 1 for x in input().split()]
    ans = 1
    cycles = []

    i = 0
    visited = [False] * n
    while i < n:
        ss = ''
        while not visited[i]:
            visited[i] = True
            ss += s[i]
            i = p[i]
        i += 1
        if len(ss) == 0:
            continue
        k = min_oper(ss)
        ans = ans * k // gcd(ans, k)

    print(ans)
