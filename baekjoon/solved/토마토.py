import collections
if __name__ == "__main__":
    N, M = map(int, input().split())
    box = []
    tomato = []
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    for i in range(M):
        tmp = list(map(int, input().split()))
        box.append(tmp)
        if 1 in tmp:
            for j in range(N):
                if tmp[j] == 1:
                    tomato.append([j, i])

    def BFS():
        dq = collections.deque()
        global box
        for i in range(len(tomato)):
            dq.append(tomato[i])

        while dq:
            position = dq.popleft()
            nx = position[0]
            ny = position[1]

            for i in range(len(dx)):
                tx = nx + dx[i]
                ty = ny + dy[i]
                if 0 <= tx < N and 0 <= ty < M:
                    if box[ty][tx] == 0:
                        dq.append([tx, ty])
                        box[ty][tx] = box[ny][nx] + 1
    BFS()
    answer = 0
    for i in range(M):
        if answer == -1:
            break
        for j in range(N):
            if box[i][j] == 0:
                answer =  -1
                break
            if box[i][j] > answer:
                answer = box[i][j]-1

    print(answer)