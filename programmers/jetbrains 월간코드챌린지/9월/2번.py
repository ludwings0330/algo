UP, RIGHT, DOWN, LEFT = [0, 1, 2, 3]
OUT, IN = [0, 1]

def solution(grid):
    answer = []
    R = len(grid)
    C = len(grid[0])
    visit = [[[False] * 4 for _ in range(C)] for _ in range(R)]

    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for r in range(R):
        for c in range(C):
            for Type in range(4):
                if not visit[r][c][Type]:
                    stack = []
                    stack.append([r, c, Type])
                    visit[r][c][Type] = True
                    cnt = 1
                    while stack:
                        current_r, current_c, current_Type = stack.pop()

                        next_r = current_r + move[current_Type][0]
                        next_c = current_c + move[current_Type][1]

                        if next_r < 0: next_r = R-1
                        elif next_r >= R : next_r = 0
                        elif next_c < 0 : next_c = C-1
                        elif next_c >= C : next_c = 0

                        ch = grid[next_r][next_c]
                        next_Type = current_Type
                        if ch == 'L':
                            next_Type = (current_Type -1 +4) %4
                        elif ch == 'R':
                            next_Type = (current_Type + 1)%4
                        if not visit[next_r][next_c][next_Type]:
                            cnt += 1
                            stack.append([next_r, next_c, next_Type])
                            visit[next_r][next_c][next_Type] = True
                        else:
                            answer.append(cnt)
                            break
    return sorted(answer)


grids = [["SL", "LR"], ["S"], ["R", "R"], ["L"], ["S", "S"]]
for grid in grids:
    print(solution(grid))