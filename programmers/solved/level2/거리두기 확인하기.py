# 응시자 P
# 빈테이블 O
# 파티션 X
# 맨해튼 거리가 2 이하로 앉지 않도록


# 거리두기 지키고 있으면 True
# 안지켜지면 False
from collections import deque

move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(place):
    board = [list(p) for p in place]

    ret = True
    for row in range(5):
        for col in range(5):
            if board[row][col] == 'P':
                visit = [[False] * 5 for _ in range(5)]
                dq = deque()
                dq.append([row, col, 0])
                # 행, 열, 거리
                while dq:
                    r, c, d = dq.pop()
                    visit[r][c] = True
                    if d > 2:
                        continue
                    if board[r][c] == 'P' and d != 0:
                        ret = False
                        break
                    for dr, dc in move:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < 5 and 0 <= nc < 5 and not visit[nr][nc] and board[r][c] != 'X':
                            dq.append([nr, nc, d + 1])

    return ret

def solution(places):
    answer = []

    for place in places:
        answer.append(1 if bfs(place) else 0)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = [1, 0, 1, 1, 1]

print(solution(places))
