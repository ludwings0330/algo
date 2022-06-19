import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    if (n + m - 1)%2 == 1:
        print("NO")
        continue
    mx = (n + m - 1) // 2
    for r in range(n):
        for c in range(m):
            if board[r][c] == -1:
                board[r][c] = 0

    for i in range(1, m):
        board[0][i] += board[0][i-1]

    rows = [set([num]) for num in board[0]]
    for r in range(1, n):
        rows[0] = set([rows[0].pop() + board[r][0]])
        for c in range(1, m):
            rows[c] = rows[c] | rows[c-1]
            if board[r][c] == 1:
                tmp = set()
                for k in rows[c]:
                    tmp.add(k+1)
                rows[c] = tmp

    if mx in rows[-1]:
        print("YES")
    else:
        print("NO")