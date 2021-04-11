if __name__ == "__main__":
    M, N = map(int, input().split())
    # M ; x ,, N ; y
    guid = []
    visit = [[0]*M for i in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    room_num = [0]
    for i in range(N):
        guid.append(list(map(int, input().split())))


    def DFS(np, num):
        stack = []
        nx = np[0]
        ny = np[1]
        tmp = 1
        global MAX
        stack.append(np)
        visit[ny][nx] = num

        while stack:
            position = stack.pop()
            nx = position[0]
            ny = position[1]
            info = guid[ny][nx]
            for i in range(4):
                if info%2 == 0: # 막혀 있지 않다면
                    tx = nx + dx[i]
                    ty = ny + dy[i]
                    if 0<=tx<M and 0<=ty<N and visit[ty][tx] == 0: # 범위 안에 있고 아직 방문하지 않았으면
                        stack.append([tx, ty])
                        visit[ty][tx] = num
                        tmp += 1
                info = int(info//2)
        room_num.append(tmp)
        if tmp > MAX:
            MAX = tmp
    num = 1
    MAX = 0

    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                DFS([j, i], num)
                num += 1
    print(num-1)
    print(MAX)

    sum_max = 0
    for y in range(N):
        for x in range(M):
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if 0<=tx<M and 0<=ty<N: # 범위 안에 들어갈때.
                    if visit[y][x] != visit[ty][tx]: # 서로 다른 방이면
                        tmp = room_num[visit[y][x]] + room_num[visit[ty][tx]]
                        if sum_max < tmp:
                            sum_max = tmp
    print(sum_max)