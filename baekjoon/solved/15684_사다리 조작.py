N, M, H = map(int, input().split())
# N : 세로선
# M : 가로선 갯수
# H : 세로선마다 가로선을 놓을 수 있는 위치의 개수
mapList = [[0]*(N+1) for _ in range(H+1)]

for i in range(M):
    # a 높이에서 b 와 b+1 이 연결되어 있음.
    a, b = map(int, input().split())
    mapList[a][b] = mapList[a][b+1] = 1

    print(mapList)

requiredLine = 0

for i in range(N):
    count = 0
    for j in range(H):
        count += mapList[j][i]
    if count %2 != 0:
        requiredLine += 1

if requiredLine > 3:
    answer = -1