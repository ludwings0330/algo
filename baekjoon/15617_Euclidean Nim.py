import sys
sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()
t = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def solve(p, q, n):
    t = n%p
    return t < q and t%(p-q) == 0

while t:
    t -= 1
    p, q, n = map(int, input().split())
    d = gcd(p, q)

    if n % d != 0:
        print('R')
        continue
    p //= d
    q //= d
    n //= d
    if p == q:
        print('E')
    elif p > q and n < p:
        print('P')
    elif p > q and n >= p:
        print('E' if solve(p, q, n) else'P')
    elif p<q and n<p:
        if n+p < q:
            print('E')
            continue
        print('P' if solve(q, p, n+p) else 'E')
    elif p<q and n >= p:
        print('E')