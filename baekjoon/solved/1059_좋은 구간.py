import sys
input = lambda: sys.stdin.readline().rstrip()

L = int(input())
S = list(map(int, input().split()))
n = int(input())

def bruteForce(S, n):
    ret = 0

    for s in range(1, 1001):
        if s > n:
            break
        for e in range(s+1, 1001):
            if e < n:
                continue
            f = True
            for ss in S:
                if s <= ss <= e:
                    f = False
                    break
            if f:
                ret += 1



    return ret



print(bruteForce(S, n))
