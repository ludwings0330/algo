import sys
input = lambda:sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
# 행, 렬
K = int(input())
DIV = 10**9 + 7

cache = [[-1] * M for _ in range(N)]

board = [[1] * M for _ in range(N)]
holes = [list(map(int, input().split())) for _ in range(K)]
for hole in holes:
    board[hole[0]-1][hole[1]-1] = 0



def jump(r, c):
    if 0 <= r < N and 0 <= c < M:
        if board[r][c] == 0:
            return 0
    else:
        return 0

    if r == N-1 and c == M-1:
        return 1

    if cache[r][c] != -1:
        return cache[r][c]

    cache[r][c] = 0
    # 짝수 번째 열
    if (c+1) % 2 == 0:
        # 짝수 번째 열
        cache[r][c] = (jump(r, c + 1) + jump(r + 1, c + 1) + jump(r + 1, c)) % DIV
    else:
        # 홀수 번째 열
        cache[r][c] = (jump(r-1, c + 1) + jump(r, c+1) + jump(r + 1 , c)) % DIV
    return cache[r][c]


print(jump(0, 0))
