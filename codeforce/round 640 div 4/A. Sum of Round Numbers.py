import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    k = 0
    ans = []
    d = 0
    while n:
        if n % 10 != 0:
            ans.append(n%10 * (10**d))
            k += 1
        d+= 1
        n //= 10

    print(k)
    print(*ans)