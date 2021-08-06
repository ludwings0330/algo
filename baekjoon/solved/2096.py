import sys
input = sys.stdin.readline

N = int(input())
INF = 987654321

sMIN = list(map(int, input().split()))
sMAX = sMIN[:]

eMIN = sMIN
eMAX = sMAX

dx = [-1, 0, 1]

for y in range(N-1):
    eMIN = [INF]*3
    eMAX = [0]*3
    line = list(map(int, input().split()))

    for x in range(3):
        for i in range(3):
            tx = x + dx[i]
            if 0 <= tx < 3:
                eMAX[tx] = max(eMAX[tx], sMAX[x] + line[tx])
                eMIN[tx] = min(eMIN[tx], sMIN[x] + line[tx])
    sMIN = eMIN
    sMAX = eMAX

print(max(eMAX), min(eMIN))