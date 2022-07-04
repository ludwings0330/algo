t = int(input())
testCase = 1

while t:
    t -= 1
    answer = 0

    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N-M+1):
        for c in range(N-M+1):
            tmp = 0
            for tr in range(r, r+M):
                for tc in range(c, c+M):
                    tmp += board[tr][tc]
            if tmp > answer:
                answer = tmp

    print(f'#{testCase} {answer}')
    testCase += 1
