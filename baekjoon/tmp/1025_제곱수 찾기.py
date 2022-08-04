import sys

input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(R)]

ans = -1
for r in range(R):
    for c in range(C):

        for dr in range(-R, R+1):
            for dc in range(-C, C+1):
                if dr == 0 and dc == 0:
                    continue
                nr = r
                nc = c
                tmp = []
                while 0 <= nr < R and 0 <= nc < C:
                    tmp.append(str(board[nr][nc]))
                    num = int(''.join(tmp))
                    if num ** 0.5 == int(num ** 0.5):
                        ans = max(ans, num)

                    nr += dr
                    nc += dc


print(ans)