# Title : 불 끄기
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')
board = []
for r in range(10):
    line = list(input())
    for i, c in enumerate(line):
        if c == 'O':
            line[i] = 1
        else:
            line[i] = 0
    board.append(line)

move =((1, 0), (-1, 0), (0, 1), (0, -1))

def push(r, c, tboard):
    tboard[r][c] ^= 1
    for i in range(4):
        tr = r + move[i][0]
        tc = c + move[i][1]
        if 0<= tr < 10 and 0 <= tc < 10:
            tboard[tr][tc] ^= 1 # 꺼져있으면 키고, 켜져있으면 끈다

def check(cnt, tboard):
    for r in range(1, 10):
        for c in range(10):
            if tboard[r-1][c] == 1: #켜져있으면
                push(r, c, tboard) #아래걸 눌러서 그 버튼을 확정 시킨다.
                cnt += 1
    for c in range(10):
        if tboard[9][c] != 0:
            return INF

    return cnt

ans = INF
def solve(c, cnt):
    if c == 10:
        global ans
        tboard = [item[:] for item in board]
        ans = min(ans, check(cnt, tboard))
        return
    push(0, c,board) # 누름
    solve(c+1, cnt + 1) # 다음
    push(0, c,board) # 누른거 취소 -> 안누름
    solve(c+1, cnt) # 다음
solve(0, 0)
print(ans)
