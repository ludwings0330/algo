import sys
input = sys.stdin.readline

T = int(input())
def gcd(a, b):
    while b!=0:
        a, b = b, a%b

    return a
def lcm(a, b):
    return a*b/gcd(a,b)
while T:
    T -= 1

    M, N, x, y = map(int, input().split())

    f = False
    a = 0
    b = 0

    K = lcm(M, N)
    while True:
        tx = x + M*a
        ty = y + N*b
        if tx > K or ty > K:
            tx = -1
            break
        elif ty < tx:
            b += 1
        elif ty > tx:
            a += 1
        elif ty == tx:
            break
    print(tx)