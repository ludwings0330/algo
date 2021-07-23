# 톱니바퀴
import sys
input = sys.stdin.readline

# 0 : N 극
# 1 : S 극

gears = []

POS = [[6, 2], [6, 2], [6, 2], [6, 2]]

for _ in range(4):
    gear = list(map(int, list(input().rstrip())))
    gears.append(gear)

K = int(input())

for _ in range(K):
    N, D = map(int, input().split())
    N -= 1
    stack = []
    stack.append([N, D])
    VISIT = [False]*4
    VISIT[N] = True

    while stack:
        n, d = stack.pop()

        if 0 <= n - 1 <= 3 and not VISIT[n - 1]:
            if gears[n - 1][POS[n - 1][1]] != gears[n][POS[n][0]]:
                stack.append([n - 1, d * (-1)])
                VISIT[n-1] = True

        if 0 <= n + 1 <= 3 and not VISIT[n + 1]:
            if gears[n + 1][POS[n + 1][0]] != gears[n][POS[n][1]]:
                stack.append([n + 1, d * (-1)])
                VISIT[n+1] = True

        POS[n][0] = (POS[n][0] - d + 8) % 8
        POS[n][1] = (POS[n][1] - d + 8) % 8

answer = 0
for i in range(4):
    score = 2**i
    index = (POS[i][1] - 2 + 8) % 8
    if gears[i][index] == 1:
        answer += score

print(answer)