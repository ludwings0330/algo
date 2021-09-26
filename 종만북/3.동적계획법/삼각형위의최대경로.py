# triangle = []
#
# def path(r, c):
#     if r == n-1:
#         return triangle[r][c]
#     if cache[r][c] != -1:
#         return cache[r][c]
#
#     ret = max(path(r+1, c), path(r+1, c+1)) + triangle[r][c]
#     cache[r][c] = ret
#     return ret
#
# n = int(input())
# cache = [[-1] * 100 for _ in range(100)]
# print(path(0, 0))


C = int(input())

def path(r, c):
    if cache[r][c] != -1:
        return cache[r][c]
    if r == N-1:
        return board[r][c]

    # 1. 아래로 내려간다.
    # 2. 오른쪽 아래로 내려간다.
    cache[r][c] = max(path(r+1, c), path(r+1, c+1)) + board[r][c]
    return cache[r][c]

for testCase in range(1, C+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    cache = [[-1] * (N+1) for _ in range(N+1)]

    print(path(0, 0))