import collections

if __name__ == "__main__":
    #   1 이동가능 0 이동불가
    #   1,1 출발 n,m 위치로 이동할때 지나야 하는 최소의 칸 수
    #   미로 크기 nxm


    n, m = map(int, input().split())
    visited = []
    for i in range(n):
        line = list(map(int, list(input())))
        visited.append(line)
    # case 1
    # n, m = 4, 6
    # visited = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def BFS():
        dq = collections.deque()
        dq.append([0, 0]) # 항상 0,0 에서 출발
        visited[0][0] = 1 # 0이면 이미 방문함.

        while dq:
            node = dq.popleft()
            nx = node[0]
            ny = node[1]
            #m 이 x 축 n 이 y축
            if nx == m-1 and ny == n-1:
                print(visited[ny][nx])
            for i in range(len(dx)):
                tx = nx+dx[i]
                ty = ny+dy[i]
                if 0 <= tx < m and 0 <= ty < n and visited[ty][tx] == 1: # map에서 1이면 갈 수 있는 길
                    dq.append([tx, ty])
                    visited[ty][tx] = visited[ny][nx] + 1

    BFS()
    pass