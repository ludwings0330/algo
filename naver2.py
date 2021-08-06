import sys

def solution(grid):
    answer = 0
    INF = sys.maxsize
    r = len(grid)
    c = len(grid[0])
    DP = [[INF]*(c+1) for _ in range(r+1)]
    DP[1][1] = grid[0][0]

    for i in range(1, r+1):
        for j in range(1, c+1):
            DP[i][j] = min(DP[i][j], DP[i-1][j] + grid[i-1][j-1], DP[i][j-1] + grid[i-1][j-1])


    answer = DP[-1][-1]


    return answer

grid = [ [1, 2], [3, 4] ]
grid2 = [ [1, 8, 3, 2], [7, 4, 6, 5] ]
grid3 = [[1], [1]]
print(solution(grid))
print(solution(grid2))
print(solution(grid3))