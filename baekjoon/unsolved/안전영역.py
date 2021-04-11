import copy
import collections
if __name__ == "__main__":
    N = int(input())
    input_map = []
    max_num = 0
    answer = []

    # 최대값 찾기.
    for i in range(N):
        input_map.append(list(map(int, input().split())))
        for j in range(N):
            if input_map[i][j] > max_num:
                max_num = input_map[i][j]

    def BFS(num):
        for level in range(num+1):
            tmp_map = copy.deepcopy(input_map)
            for i in range(N):
                for j in range(N):
                    if tmp_map[i][j] <= level:
                        tmp_map[i][j] = 0
            answer.append(0)
            while True:
                dq = []
                nx, ny = -1, -1
                dx = (0, 1, 0, -1)
                dy = (1, 0, -1, 0)

                for i in range(N):
                    if nx != -1:
                        break
                    for j in range(N):
                        if tmp_map[i][j] != 0:
                            nx = j
                            ny = i
                            break
                if nx == -1:
                    break
                dq = collections.deque()
                dq.append([nx, ny])
                tmp_map[ny][nx] = 0
                while dq:
                    location = dq.popleft()
                    nx = location[0]
                    ny = location[1]
                    for i in range(4):
                        tx = nx + dx[i]
                        ty = ny + dy[i]
                        if 0<=tx<N and 0<=ty<N and tmp_map[ty][tx] !=0: # 방문하지 않았으면
                            dq.append([tx, ty])
                            tmp_map[ty][tx] = 0 # 방문 표시
                answer[level] += 1

    # 물에잠기지않는 최대 경우.
    BFS(max_num)
    answer.sort(reverse=True)
    print(answer[0])