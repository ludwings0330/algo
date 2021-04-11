if __name__ == "__main__":
    N = int(input())
    i_map = []
    for i in range(N):
        i_map.append(list(map(int, list(input()))))
    answer = []
    numbers = 0
    def BFS(number):
        while True:
            dq = []
            nx, ny = -1, -1
            dx = (0, 1, 0, -1)
            dy = (1, 0, -1, 0)

            for i in range(N):
                for j in range(N):
                    if i_map[j][i] == 1:
                        nx = i
                        ny = j
                        break
            if nx == -1:
                break

            answer.append(0)
            dq.append([nx, ny])
            i_map[ny][nx]=0
            answer[number]+=1
            while dq:
                location = dq.pop(0)
                nx = location[0]
                ny = location[1]

                for i in range(4):
                    tx = nx + dx[i]
                    ty = ny + dy[i]
                    if 0 <= tx < N and 0<=ty<N and i_map[ty][tx]!=0: # 방문 안한곳만

                        dq.append([tx, ty])
                        i_map[ty][tx] = 0 # 방문처리
                        answer[number] += 1
            number += 1

    BFS(0)
    print(len(answer))
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])

