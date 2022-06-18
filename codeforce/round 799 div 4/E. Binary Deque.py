import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)

    if total < s:
        print(-1)
        continue
    elif total == s:
        print(0)
        continue

    for i in range(n):
        if i:
            a[i] += a[i-1]

    ans = float('inf')
    for i in range(n):
        left = i
        right = n - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            tmp = a[mid] - (a[i-1] if i else 0)
            if tmp <= s:
                pos = mid
                left = mid + 1
            else:
                right = mid - 1
        tmp = a[pos] - (a[i-1] if i else 0)
        if pos == -1 or tmp != s:
            continue

        ans = min(ans, n - (pos - i + 1))
    print(ans)
