
def solution(key, lock):
    ret = False

    N = len(lock)
    M = len(key)

    biglock = [[0] * (N*3) for _ in range(N*3)]
    hole = 0
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            biglock[i][j] = lock[i-N][j-N]
            if biglock[i][j] == 0:
                hole += 1

    def check(x, y, r): # r = 0 ? 0도 회전 r = 1? 90도 회선 r =2 ? 180도 회전, r = 3 ? 270도 회전
        c = 0
        if r == 0:
            for i in (range(y, y+M)):
                for j in (range(x, x+M)):
                    if N <= i < 2*N and N <= j < 2*N:
                        if key[i-y][j-x] ==1 and biglock[i][j] == 0:
                            c += 1

        elif r == 1:
            for i in (range(y, y + M)):
                for j in (range(x, x + M)):
                    if N <= i < 2 * N and N <= j < 2 * N:
                        if key[j-x][i - y] ==1 and biglock[j][i] == 0:
                            c += 1

        elif r == 2:
            for i in (range(y+M-1, y-1, -1)):
                for j in (range(x+M-1, x-1, -1)):
                    if N <= i < 2 * N and N <= j < 2 * N:
                        if key[j - x][i - y] ==1 and biglock[j][i] == 0:
                            c += 1
        else:
            for i in (range(y + M - 1, y - 1, -1)):
                for j in (range(x + M - 1, x - 1, -1)):
                    if N <= i < 2 * N and N <= j < 2 * N:
                        if key[i - y][j - x] == 1 and biglock[i][j] == 0:
                            c += 1

        if c == hole:
            print(x,  y, r)
            return True
        else:
            return False


    for y in range(N-M-1, 2*N):
        for x in range(N-M-1, 2*N):
            for i in range(4):
                if check(x, y, i):
                    return True


    return ret

key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]

lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

print(solution(key, lock))