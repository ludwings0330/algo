import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
from collections import deque

while t:
    t -= 1
    n, k = map(int, input().split())
    board = input()
    flag = False
    for ss in board.split('W'):
        if len(ss) >= k:
            print(0)
            flag = True
            break
    if flag:
        continue

    tmp = [0] * (n)
    for i in range(n):
        if board[i] == 'W':
            tmp[i] = 1
        elif board[i] == 'B':
            if i != 0 and board[i-1] == 'B':
                tmp[i], tmp[i-1] = tmp[i-1] + 1, -1
            else:
                tmp[i] = 1
    dq = deque()

    # idx, recolored, length
    for i in range(n):
        if tmp[i] != -1:
            dq.append([i, 0 if board[i] == 'B' else 1, tmp[i]])

    while dq:
        idx, recolored, length = dq.popleft()
        if length >= k:
            print(recolored)
            break

        if idx + 1 < n:
            dq.append([idx+1, recolored + (0 if board[idx+1] == 'B' else 1), length + 1])
