import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for test_case in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    for i in range(len(a) - 1, 0, -1):
        a[i-1] += a[i]

    for query in range(q):
        target = int(input())
        answer = -1

        left = 0
        right = len(a)
        while left < right:
            mid = (left + right) // 2

            if target <= a[mid]:
                left = mid + 1
                answer = len(a) - mid
            else:
                right = mid
        print(answer)