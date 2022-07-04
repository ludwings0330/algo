import heapq

TC = int(input())
move = [(1, 0), (0, 1), (0, -1), (-1, 0)]
def dijkstra(start):
    hq = [(0, 0, 0)]
    dists[0][0] = 0

    while hq:
        current_v, current_r, current_c = heapq.heappop(hq)



        for dr, dc in move:
            next_r = current_r + dr
            next_c = current_c + dc

            if 0 <= next_r < N and 0 <= next_c < N: # board 안에 들어가야함
                next_v = current_v + board[next_r][next_c]
                if dists[next_r][next_c] > next_v: # 더 비용이 낮은 방법을 알았을때 바꿔준다
                    dists[next_r][next_c] = current_v
                    if next_r == next_c == N - 1:
                        return
                    heapq.heappush(hq, (next_v, next_r, next_c))

INF = float('inf')
for testCase in range(1, TC+1):
    print("#{}".format(testCase), end =' ')

    N = int(input())
    board = []
    dists = [[INF] * N for _ in range(N)]

    for _ in range(N):
        line = list(map(int, list(input())))
        board.append(line)

    dijkstra([0, 0])
    print(dists[-1][-1])