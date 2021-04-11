# T : test case
# M : 열 (가로길이)
# N : 행 (세로길이)
# K : 배추가 심어진 개수
import sys

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

if __name__ == "__main__":
    T = int(input())
    while T > 0:
        M, N, K = map(int, input().split())
        veges = [[0]*M for i in range(N)]
        for i in range(K):
            x, y = map(int, sys.stdin.readline().rstrip().split())
            veges[y][x] = 1


        def DFS(x, y, veges):
            stack = []
            stack.append([x, y])
            veges[y][x] = 0
            global M, N

            while stack:
                node = stack.pop()
                nx = node[0]
                ny = node[1]
                for i in range(len(dx)):
                    tx = nx + dx[i]
                    ty = ny + dy[i]
                    if 0 <= tx < M and 0 <= ty < N and veges[ty][tx] == 1:
                        stack.append([tx, ty])
                        veges[ty][tx] = 0

            return 1

        count = 0

        for y in range(N):
            for x in range(M):
                if veges[y][x] == 1:
                    count += DFS(x, y, veges)
        T -= 1
        print(count)