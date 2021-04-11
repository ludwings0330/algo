import copy
if __name__=="__main__":
    # y 12줄 x 6개
    field = []
    Y = 12
    X = 6
    visit = [[0]*X for i in range(Y)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    combo = 0

    for i in range(Y):
        field.append(list(input()))


    def DFS(nx, ny, combo):
        stack = []
        stack.append([nx, ny])
        tmp_visit = copy.deepcopy(visit)
        tmp_field = copy.deepcopy(field)

        ch = tmp_field[ny][nx]  # 현재 글자.
        tmp_field[ny][nx] = '.'
        tmp_visit[ny][nx] = 1
        count = 1
        while stack:
            position = stack.pop()
            nx = position[0]
            ny = position[1]
            for i in range(len(dx)):
                tx = nx + dx[i]
                ty = ny + dy[i]
                if 0 <= tx < X and 0 <= ty < Y and ch == tmp_field[ty][tx] and tmp_visit[ty][tx] == 0:
                    stack.append([tx, ty])
                    tmp_field[ty][tx] = '.'
                    tmp_visit[ty][tx] = 1
                    count+=1
        if count >= 4:
            print("뿌셔뿌셔")
            print(tmp_field)
            combo += 1

    for i in range(Y-1,0,-1):
        for j in range(X):
            if field[i][j] != '.':
                DFS(j, i, combo)