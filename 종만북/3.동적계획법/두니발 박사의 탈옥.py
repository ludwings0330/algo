c = int(input())
for testCase in range(1, c+1):
    n, d, p = map(int, input().split())
    # n 마을의 수, d 탈출 후 지금까지 지난 일 수, p : 교도소가 있는 마을의 번호

    connected = [[-1]*(n+1) for _ in range(n+1)]
    deg = [0] * (n+1)
    for i in range(n):
        line = list(map(int, input().split()))

        for j in range(n):
            connected[i+1][j+1] = line[j]
            if line[j] == 1:
                deg[j] += 1
    print(deg)