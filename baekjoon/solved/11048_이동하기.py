import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cache = [[-1] * M for _ in range(N)]

def move(r, c):
    if 0 <= r < N and 0 <= c < M:
        pass
    else:
        return 0

    if r == N-1 and c == M-1:
        return board[r][c]

    if cache[r][c] != -1:
        return cache[r][c]

    cache[r][c] = board[r][c]

    cache[r][c] += max(move(r+1, c), move(r, c+1), move(r+1, c+1))

    return cache[r][c]

print(move(0, 0))


