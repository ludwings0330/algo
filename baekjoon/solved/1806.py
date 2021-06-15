import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0

LEN = sys.maxsize
SUM = arr[0]

while True:
    if e == s:
        e += 1
    if SUM >= S:
        LEN = min(LEN, e-s)
        SUM -= arr[s]
        s += 1
    else:
        if e < N:
            SUM += arr[e]
            e += 1
        else:
            break

if LEN == sys.maxsize:
    print(0)
else:
    print(LEN)