import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
# R, C <= 50
board = [list(input()) for _ in range(R)]
cache = [[-1] * C for _ in range(R)]
move = ((0, 1), (0, -1), (1, 0), (-1, 0))
visited = [[False] * C for _ in range(R)]


# 현재 위치가 r, c 일때 동전을 움직일 수 있는 최대 횟수
# cache[r][c] = max(cache[r+t][c], cache[r][c+t], cache[r-t][c], cache[r][c-t]) + 1
def solve(r, c):
    if 0 <= r < R and 0 <= c < C:
        pass
    else:
        # 범위를 벗어난 경우는 제외
        return 0

    # 현재 위치가 구멍이라면 제외
    if board[r][c] == 'H':
        return 0

    # 방문한적 있다면 -1 (싸이클이 생긴다면)
    if visited[r][c]:
        return -1

    # 이미 구한적 있다면 그대로 반환
    if cache[r][c] != -1:
        return cache[r][c]

    cache[r][c] = 0
    visited[r][c] = True
    size = int(board[r][c])
    for tr, tc in move:
        nr = r + tr * size
        nc = c + tc * size
        ret = solve(nr, nc)

        if ret == -1:
            return -1
        cache[r][c] = max(cache[r][c], ret + 1)
    visited[r][c] = False
    return cache[r][c]

print(solve(0, 0))
