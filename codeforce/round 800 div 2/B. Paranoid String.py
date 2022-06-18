import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    s = list(input())
    ans = n
    for i in range(1, n):
        if s[i] != s[i-1]:
            ans += i
    print(ans)

