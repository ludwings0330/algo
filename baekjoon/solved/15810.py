import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
A = list(map(int, input().split()))


def binary_search(target):
    left = 1
    right = M * 1_000_000
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for a in A:
            cnt += mid//a
            if cnt > target:
                break
        if cnt >= target:
            right = mid - 1
        else:
            left = mid + 1

    return left


print(binary_search(M))