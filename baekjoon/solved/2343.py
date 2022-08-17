import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 100_000 * 10_000

while left < right:
    mid = (left + right) // 2
    size = 0
    m = 1

    for i in range(N):
        if size + arr[i] <= mid:
            size += arr[i]
        else:
            # 블루에이에 담을 수 없다면 더 커야한다.
            if arr[i] > mid:
                m = float('inf')
                break
            size = arr[i]
            m += 1
        if m > M:
            break

    if m > M:
        left = mid + 1
    else:
        right = mid

print(left)
