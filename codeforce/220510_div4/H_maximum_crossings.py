import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())


for test_case in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    stack = [a[0]]
    answer = 0
    for target in a[1:]:
        left = 0
        right = len(stack) - 1

        while left < right:
            mid = (left + right)//2
            if a[mid] < target:
                left = mid + 1
            else:
                right = mid
        answer += len(stack) - right
        stack.insert(right, target)

    print(answer)