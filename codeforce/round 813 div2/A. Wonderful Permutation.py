import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(k):
        if 1 <= arr[i] <= k:
            pass
        else:
            cnt += 1
    print(cnt)