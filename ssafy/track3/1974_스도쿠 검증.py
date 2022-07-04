tc = int(input())
for test_case in range(tc):
    board = [list(map(int, input().split())) for _ in range(9)]
    answer = 1

    for r in range(9):
        check_r = set()
        for c in range(9):
            if board[r][c] in check_r:
                answer = 0
            else:
                check_r.add(board[r][c])

    for c in range(9):
        check_c = set()
        for r in range(9):
            if board[r][c] in check_c:
                answer = 0
            else:
                check_c.add(board[r][c])

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            check_box = set()
            for tr in range(r, r+3):
                for tc in range(c, c+3):
                    check_box.add(board[tr][tc])
            if len(check_box) != 9:
                answer = 0

    print(f'#{test_case+1} {answer}')
