#
import sys
input = sys.stdin.readline

N = int(input())

abil = []

for _ in range(N):
    abil.append(list(map(int, input().split())))

# 능력치 차이가 최소가 되도록.
MIN = sys.maxsize

def abilitySum():
    SUM = 0

    for i in range(N):
        for j in range(N):
            if visit[i] and visit[j]:
                SUM += abil[i][j]
            elif not visit[i] and not visit[j]:
                SUM -= abil[i][j]

    global MIN
    MIN = min(MIN, abs(SUM))

visit = [False]* (N)

def solve(i, pick):
    if pick == int(N/2):
        abilitySum()
        return
    e = int(N/2)+i
    if e>=N:
        e = N
    for j in range(i+1, e):
        if not visit[j]:
            visit[j] = True
            solve(j, pick+1)
            visit[j] = False
solve(0, 0)
print(MIN)
