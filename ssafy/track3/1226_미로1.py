move = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dfs(start):
    stack = [start]
    ret = False
    visit = set()
    visit.add(tuple(start))
    while stack:
        r, c = stack.pop()
        if board[r][c] == 3:
            ret = True
            break

        for dr, dc in move:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 16 and 0 <= nc < 16 and board[nr][nc] != 1 and (nr, nc) not in visit:
                stack.append([nr, nc])
                visit.add((nr, nc))

    return ret


for test_case in range(1, 11):
    ans = 0
    input()
    board = [list(map(int, list(input()))) for _ in range(16)]
    start = [0, 0]

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 2:
                start = [r, c]

    if dfs(start):
        ans = 1

    print(f'#{test_case} {ans}')