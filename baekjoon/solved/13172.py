import sys
input = sys.stdin.readline

M = int(input())
dice = [list(map(int, input().split())) for _ in range(M)]

X = 1000000007
EV = 0 # expected value 기대값

def getinverse(b, n):
    if n == 0:
        return 1
    elif n == 1:
        return b

    if n % 2 == 1:
        a = getinverse(b, n // 2)
        c = a * b
        return (a * c) % X
    else:
        a = getinverse(b, n // 2)
        return (a * a) % X

def solve(a, b):
    # 1. b 의 역원을 구한다.
    # 2. Q = a*b^-1 (mod X) 를 구한다.
    inverseb = getinverse(b, X-2)
    Q = (a*inverseb) % X
    return Q

for b, a in dice:
    EV = (EV + solve(a, b)) % X
print(EV)