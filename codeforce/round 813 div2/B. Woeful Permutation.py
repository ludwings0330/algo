import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    n = int(input())
    if n == 1:
        ans = [0, 1]
    elif n == 2:
        ans = [0, 2, 1]
    else:
        ans = [0] * (n+1)
        ans[1] = 1
        if n % 2 == 1:
            for i in range(2, n+1, 2):
                ans[i] = i+1
                ans[i+1] = i
        else:
            for i in range(1, n+1, 2):
                ans[i] = i+1
                ans[i+1] = i
    print(*ans[1:])
    t -= 1