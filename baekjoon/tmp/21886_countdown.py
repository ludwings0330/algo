N, S = map(int, input().split())
A = list(map(int, input().split()))


def count(k):
    ret = 0
    for i in range(N):
        ret += max(0, k-A[i])
    return ret


left, right = 0, S
mid = 0

while left < right:
    mid = (left + right) // 2

    expect_time = count(mid)
    if expect_time == S:
        left = mid
        break
    elif expect_time < S:
        left = mid + 1
    elif expect_time > S:
        right = mid - 1

print(left)