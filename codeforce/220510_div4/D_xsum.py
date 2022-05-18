import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

t = int(input())

for test_case in range(t):
    r, c = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(r)]

    sum_r = defaultdict(int)
    sum_l = defaultdict(int)
    for row in range(r):
        for col in range(c):
            sum_r[row-col] += board[row][col]
            sum_l[row+col] += board[row][col]


    answer = 0
    for row in range(r):
        for col in range(c):
            answer = max(answer, sum_r[row-col] + sum_l[row+col] - board[row][col])

    print(answer)