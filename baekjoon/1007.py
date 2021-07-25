import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())
while TC:
    TC -= 1
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    