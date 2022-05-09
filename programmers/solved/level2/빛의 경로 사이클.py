from collections import deque

# S : 직진, L : 좌회전, R : 우회전

# 1<= grid <= 500

# (r, c)
move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
visit = [[[False] * 4 for _ in range(len(board[0]))] for _ in range(len(board))]

def cycle(r, c, d):
    ret = 0

    dq = deque()
    dq.append([r, c, d])
    
def solution(grid):
    answer = []
    board = [list(g) for g in grid]


    global visit

    for r in range(len(board)):
        for c in range(len(board[0])):
            for d in range(4): # 0 : 위, 1 : 왼, 2: 아래, 3: 오른쪽
                if not visit[r][c][d]:
                    visit[r][c][d] = 0
                    answer.append(cycle(r, c, d))

    answer.sort()
    return answer


grid = [["SL", "LR"], ["S"], ["R", "R"]]

for i in range(len(grid)):
    print(solution(grid[i]))
