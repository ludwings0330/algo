import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

ans = []

A.reverse()

ans = [-1]
stack = [A[0]]

for i in range(1, N):
    if stack[-1] > A[i]:
        ans.append(stack[-1])

    else:
        while stack and stack[-1] <= A[i]:
            stack.pop()
        if not stack:
            stack.append(-1)
        ans.append(stack[-1])
    stack.append(A[i])

ans.reverse()
print(*ans)