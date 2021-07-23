import sys
input = sys.stdin.readline

# r, c
N, M = map(int, input().split())
# N 세로크기 M 가로크기
board = []
robot = list(map(int, input().split()))
visit = [[False]*M for _ in range(N)]

# 0 위, 1 오른, 2 아래, 3 왼
dd = [[0, -1], [1, 0], [0, 1], [-1, 0]]

for _ in range(N):
    board.append(list(map(int, input().split())))

ans = 0

while True:
    r, c, d = robot
    if not visit[r][c]:
        visit[r][c] = True
        ans += 1

    for i in range(1, 5): # 총 4번 돌아야지
        #현재 방향기준 왼쪽 방향부터 탐색
        td = d-i if d-i >= 0 else 4 + d - i

        tr = r + dd[td][1]
        tc = c + dd[td][0]
        if 0 <= tr < N and 0 <= tc < M: # 범위 안에 있으면 이동
            if board[tr][tc] != 1: # 탐색하는 곳이 벽이 아니면
                if not visit[tr][tc]: # 왼쪽이 아직 청소하지 않았다면
                    robot = [tr, tc, td] # 방향을 바꾸고 로봇을 이동한다.
                    board[r][c] = 0
                    board[tr][tc] = 2
                    break
                else: # 이미 청소 했으면
                    continue
    else: # 이동을 하지 않았다면 후진
        tr = r - dd[d][1]
        tc = c - dd[d][0]
        if board[tr][tc] == 1: # 뒤가 벽이라 후진 못하면
            break # 종료
        else: # 후진 가능하면
            robot = [tr, tc, d] #그냥 후진해준다.
            board[r][c] = 0
            board[tr][tc] = 2

print(ans)