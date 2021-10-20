import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**9)

'''
점프를 하면 현재 위치에 적힌 숫자 만큼 오른쪽이나 아래로 점프를 한다.
이때 N-1, N-1 에 도착하는 경우의 수

1. 오른쪽으로 뛰기
2. 아래로 뛰기

'''
def jump(x, y):
    if 0 <= x < N and 0 <= y < N:
        pass
    else:
        return 0

    if x == N-1 and y == N-1:
        return 1

    if cache[x][y] != -1:
        return cache[x][y]

    if board[y][x] == 0:
        cache[x][y] = 0
    else:
        cache[x][y] = jump(x + board[y][x], y) + jump(x, y + board[y][x])

    return cache[x][y]

N = int(input())
cache = [[-1] * (N+1) for _ in range(N+1)]
board = [list(map(int, input().split())) for _ in range(N)]

print(jump(0, 0))
