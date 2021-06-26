def recursiveSolve(N, x, y):
    global starBoard

    if N == 1:
        starBoard[y][x] = '*'
        return
    nextNum =  N//3

    for dy in range(3):
        for dx in range(3):
            if dx == 1 and dy == 1:
                pass
            else:
                recursiveSolve(nextNum, x+dx*nextNum, y+dy*nextNum)

N = int(input())
starBoard = [[' '] * N for _ in range(N)]

# N/3 개로 나눠서 중앙만 비고 나머지는 꽉차있는 형태.
recursiveSolve(N, 0, 0)
for i in range(N):
    print(''.join(starBoard[i]))

