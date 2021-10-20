import sys
input = lambda: sys.stdin.readline().rstrip()


N = int(input())
board = [list(input()) for _ in range(N)]

ans = [-1, -1, 0]

'''
갯수가 같다면
1. y좌표가 작은것
2. y좌표가 같으면 x좌표가 작은것 출력
'''

move = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))

def check(r, c):
    ret = 0


    for [dr, dc] in move:
        cnt = 0
        tr, tc = r+dr, c+dc

        while 0 <= tr < N and 0 <= tc < N:
            if board[tr][tc] == 'W':
                cnt += 1
            elif board[tr][tc] == 'B':
                ret += cnt
                break
            elif board[tr][tc] == '.':
                break
            tr = tr + dr
            tc = tc + dc

    return ret

for r in range(N):
    for c in range(N):
        if board[r][c] == '.':
            cnt = check(r, c)
            if cnt >= ans[-1]:
                if cnt > ans[-1]:
                    ans[0] = c
                    ans[1] = r
                    ans[2] = cnt
                else:
                    if ans[1] > r:
                        ans[0] = c
                        ans[1] = r
                    elif ans[1] == r:
                        if ans[0] > c:
                            ans[0] = c
                            ans[1] = r
if ans[-1] == 0:
    print("PASS")
else:
    print("%d %d\n%d" %(ans[0], ans[1], ans[2]))

