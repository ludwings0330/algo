import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)

str_find = input()
LEN = len(str_find)
N, M = map(int, input().split())
board = []

for _ in range(M):
    line = list(input())
    board.append(line)

move = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
stack = []

def dfs(r, c, idx, path):
    if idx == LEN:
        return True

    if board[r][c] == str_find[idx]:
        (dr, dc) = move[path]
        tr = r + dr
        tc = c + dc
        if 0 <= tr < M and 0 <= tc < N:
            if dfs(tr, tc, idx + 1, path):
                return True
    return False

isAnswer = False

for r in range(M):
    for c in range(N):
        for m in range(8):
            if dfs(r, c, 0, m):
                isAnswer = True
                break
        if isAnswer:
            break
    if isAnswer:
        break
print(1 if isAnswer else 0)
