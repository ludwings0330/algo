import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

board = [[0] * N for _ in range(N)]
plants = []
for _ in range(M):
    X, Y, L, F = map(int, input().split())
    for r in range(Y, Y+L):
        for c in range(X, X+L):
            board[r][c] = F
    plants.append([X, Y, L, F])

plants.sort(key=lambda x:x[2], reverse=True)

for C, R, L, _ in plants:
    cnt = set()
    for r in range(R, R+L):
        for c in range(C, C+L):
            cnt.add(board[r][c])
    if len(cnt) <= 2:
        print(L*L)
        break
