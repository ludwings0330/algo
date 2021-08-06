import sys

input = sys.stdin.readline

N, M, H = map(int, input().split())
# N 세로선 갯수 M 가로선 갯수, H 가로선을 놓을 수 있는 위치의 개수
# 2 <= N <= 10, 1 <= H <= 30, 0 <= M <= (N-1)xH
canPut = [[True] * N for _ in range(M)]
line = []
for _ in range(H):
    a, b = map(int, input().split())
    # b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결하겠다는 뜻
    line.append([a, b])