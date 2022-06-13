import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())
    board = []

    for _ in range(n):
        board.append(list(input()))
