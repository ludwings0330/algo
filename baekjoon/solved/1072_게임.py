import sys
input = lambda: sys.stdin.readline().rstrip()
X, Y = map(int, input().split())


def binary_search(X, Y):
    Z = int((Y*100/X))
    left = 1
    right = 10**9
    while left <= right:
        mid = (left + right) // 2
        nZ = int((Y+mid)*100/(X+mid))
        if nZ == Z:
            left = mid + 1
        elif nZ > Z:
            right = mid - 1
    return left


if Y/X * 100 >= 99:
    print(-1)
else:
    print(binary_search(X, Y))