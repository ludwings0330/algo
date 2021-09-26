C = int(input())

def jump(r, c):
    if r >= N or c >= N:
        return False

    if r == N-1 and c == N-1:
        return True

    if cache[r][c] != -1:
        return cache[r][c]

    jumpSize = board[r][c]
    cache[r][c] = jump(r + jumpSize, c) or jump(r, c + jumpSize)

    return cache[r][c]


for testCase in range(1, C+1):
    N = int(input())

    cache = [[-1] *(N+1) for _ in range(N+1)]
    board = []

    for i in range(N):
        board.append(list(map(int, input().split())))

    if jump(0, 0):
        print('YES')
    else:
        print('NO')

