import sys
import copy
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [[0, 0, 0]]
for _ in range(N):
    board.append(list(map(int, input().split())))

INF = 987654321
MIN = INF

for n in range(3):
    tboard = copy.deepcopy(board)
    for k in range(3):
        if n != k:
            tboard[1][k] = INF
        else:
            tboard[-1][k] = INF

    for i in range(1, N+1):
        tboard[i][0] += min(tboard[i - 1][1], tboard[i - 1][2])
        tboard[i][1] += min(tboard[i - 1][0], tboard[i - 1][2])
        tboard[i][2] += min(tboard[i - 1][0], tboard[i - 1][1])

    MIN = min(tboard[-1]+[MIN])
print(MIN)