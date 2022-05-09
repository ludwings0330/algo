from collections import deque
# 최단 거리 -> BFS


def solution(maps):
    answer = -1
    dq = deque()
    n = len(maps)
    m = len(maps[0])
    # r, c, l
    visit = [[False] * m for _ in range(n)]
    dq.append([0, 0, 1])
    visit[0][0] = True

    move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while dq:
        r, c, l = dq.popleft()

        if r == n-1 and c == m-1:
            answer = l
            break

        for dr, dc in move:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and not visit[nr][nc]:
                visit[nr][nc] = True
                dq.append([nr, nc, l + 1])

    return answer


maps = [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],
        [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]

for m in maps:
    print(solution(m))
