import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())

    frequency = n - 1
    count = k // frequency
    remains = k % frequency

    ans = n * count + (remains if remains != 0 else -1)
    print(ans)
