import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())
    # row, col
    board = [list(map(int, input().split())) for _ in range(n)]

    mx = -float('inf')
    mx_r, mx_c = 0, 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if mx < board[r][c]:
                mx = board[r][c]
                mx_r = r
                mx_c = c
    mx_r += 1
    mx_c += 1
    print(max((n-mx_r+1) * (mx_c), (n-mx_r+1) * (m - mx_c+1), (mx_r) * (mx_c), (mx_r * (m - mx_c+1))))

