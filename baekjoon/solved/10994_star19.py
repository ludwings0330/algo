N = int(input())

starMap = [[' ']* (4*N -3) for i in range(4*N -3)]


def recursiveSolve(n, x, y):
    if n == 1:
        starMap[y][x] = '*'
        return

    len = 4*n - 3

    for i in range(y, y+len):
        starMap[x][i] = '*'
        starMap[x+len-1][i] = '*'
    for j in range(x, x+len):
        starMap[j][y] = '*'
        starMap[j][y+len-1] = '*'

    recursiveSolve(n-1, x+2, y+2)
    return

recursiveSolve(N, 0, 0)

for i in range(len(starMap)):
    print(''.join(starMap[i]))