'''
스도쿠

1. 빈칸 찾기
2. 빈칸에 1~9 대입
3. 가로 확인
4. 세로 확인
5. 사각형 범위 확인
6. 모두 가능하면 다음 빈칸으로 이동,
7. 불가능하면 다음 숫자 대입

'''

import sys
input = lambda: sys.stdin.readline().rstrip()

board = [list(map(int, input().split())) for _ in range(9)]
toPick = 0
blanks = []

for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            toPick += 1
            blanks.append([r, c])

def findCandidate(r, c):
    ret = set()

    for i in range(9):
        ret.add(board[r][i])
        ret.add(board[i][c])

    for tr in range(r//3*3, r//3*3+3):
        for tc in range(c//3*3, c//3*3+3):
            ret.add(board[tr][tc])

    return set(i for i in range(10)) - ret


def sudoku(idx, toPick):
    if toPick == 0:
        for line in board:
            print(*line)
        return True

    [r, c] = blanks[idx]

    '''
    check 가 너무 쓰잘데기 없이 반복된다.
    (r, c) 에 들어갈 수 있는 숫자만 걸러내서 check 하기 
    candidates
    '''
    candidates = findCandidate(r, c)
    for i in candidates:
        board[r][c] = i

        if sudoku(idx+1, toPick - 1):
            return True

        board[r][c] = 0

    return False

sudoku(0, toPick)