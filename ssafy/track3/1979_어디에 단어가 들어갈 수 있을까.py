T = int(input())
testCase = 1
def check_row(r, c, n, k):
    count = 0
    for t in range(r, n):
        if board[t][c] == 1:
            count += 1
        else:
            break

    return count == k


def check_col(r, c, n, k):
    count = 0
    for t in range(c, n):
        if board[r][t] == 1:
            count +=1
        else:
            break

    return count == k


while T:
    T -= 1
    answer = 0

    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                if r == 0 or (r != 0 and board[r-1][c] == 0):
                    if check_row(r, c, N, K):
                        answer += 1
                if c == 0 or (c != 0 and board[r][c-1] == 0):
                    if check_col(r, c, N, K):
                        answer += 1

    print(f'#{testCase} {answer}')
    testCase += 1
