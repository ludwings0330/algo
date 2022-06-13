import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    board = input()

    ans = 0
    for i in range(0, k):
        ans += 1 if board[i] == 'W' else 0

    tmp = ans
    for i in range(k, n):
        if board[i-k] == 'W':
            tmp -= 1
        if board[i] == 'W':
            tmp += 1
        ans = min(ans, tmp)

    print(ans)
