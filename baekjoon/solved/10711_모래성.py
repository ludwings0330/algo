import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())

board = [list(input()) for _ in range(H)]

dq = deque()
move = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

def checkAround(r, c):
    cnt = 0

    for i in range(len(move)):
        tr = r + move[i][0]
        tc = c + move[i][1]
        if 0 <= tr < H and 0 <= tc < W and board[tr][tc] == '.':
           cnt += 1

    if cnt >= int(board[r][c]):
        return True

    return False

for r in range(H):
    for c in range(W):
        if board[r][c] != '.' and checkAround(r, c):
            dq.append([r, c, 1])



# True면 모래성이 파괴된다
# False면 모래성이 파괴되지 않는다.
wave = 0
while dq:
    r, c, cnt = dq.popleft()
    if board[r][c] == '.':
        continue

    wave = max(wave, cnt)
    # 모래성이  파괴된다면 주변 방향을 모두 넣고 다시 ㄱㄱ

    # 모래성이 무너지고, 근처에 무너질 가능성이 있는 애들을 모두 넣어줘.
    board[r][c] = '.'
    for i in range(len(move)):
        tr = r + move[i][0]
        tc = c + move[i][1]
        if 0 <= tr < H and 0 <= tc < W and board[tr][tc] != '.' and checkAround(tr, tc):
            dq.append([tr, tc, cnt + 1])


print(wave)