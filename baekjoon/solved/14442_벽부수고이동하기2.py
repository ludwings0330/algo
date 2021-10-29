'''
6 4 1
0100
1110
1000
0000
0111
0000

15

7 5 2
00000
11110
00000
11111
00000
01111
00000
'''
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

R, C , K = map(int, input().split())
board = [ list(map(int, list(input()))) for _ in range(R)]
cache = [[[-1] * C for _ in range(R)] for _ in range(K+1)]

dq = deque()
dq.append([0, 0, K])
cache[K][0][0] = 1

move = ((1, 0), (-1, 0), (0, 1), (0, -1))
while dq:
    r, c, k = dq.popleft()

    if r == R-1 and c == C-1:
        break

    for i in range(len(move)):
        tr = r + move[i][0]
        tc = c + move[i][1]

        if 0 <= tr < R and 0 <= tc < C:
            # 다음으로 이동이 가능하면
            # 다음이 벽이면
            if board[tr][tc] == 1:
                # 부수기 횟수가 남아있으면 부수고 이동 가능
                if k > 0:
                    # 다음이 한번도 안가본 길이거나, 지금 방법이 더 빠르면
                    if cache[k-1][tr][tc] == -1 or cache[k-1][tr][tc] > cache[k][r][c] + 1:
                        dq.append([tr, tc, k-1])
                        cache[k-1][tr][tc] = cache[k][r][c] + 1
                # 남아있찌 않으면
                else:
                    # 벽인데 부술수 없으면 못가는거지
                    pass
            # 다음이 벽이 아니면
            else:
                # 한번도 안가봤거나, 지금 방법이 더 빠르면
                if cache[k][tr][tc] == -1 or cache[k][tr][tc] > cache[k][r][c] + 1:
                    dq.append([tr, tc, k])
                    cache[k][tr][tc] = cache[k][r][c] + 1

ans = 987654321
for k in range(K+1):
    if cache[k][R-1][C-1] != -1:
        ans = min(ans, cache[k][R-1][C-1])
print(ans if ans != 987654321 else -1)