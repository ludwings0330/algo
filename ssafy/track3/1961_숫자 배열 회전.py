tc = int(input())
testCase = 1
while tc:
    tc -= 1
    N = int(input())
    answer = [[-1]*3 for _ in range(N)]

    board = [list(map(int, input().split())) for _ in range(N)]

    for t in range(N):
        tmp = []
        for k in range(N-1, -1, -1):
            tmp.append(str(board[k][t]))
        answer[t][0] = ''.join(tmp)

    for t in range(N):
        tmp = []
        for k in range(N-1, -1, -1):
            tmp.append(str(board[N-1-t][k]))
        answer[t][1] = ''.join(tmp)

    for t in range(N):
        tmp = []
        for k in range(N):
            tmp.append(str(board[k][N-1-t]))
        answer[t][2] = ''.join(tmp)

    print(f'#{testCase}')
    testCase += 1

    # print answer
    for ans in answer:
        print(*ans)