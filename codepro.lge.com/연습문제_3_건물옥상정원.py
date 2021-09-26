import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
H = []
stack = []

for _ in range(N):
    H.append(int(input()))


ans = 0
MAX = 0
for i in range(N):
    if not stack or H[i] > MAX: # 비어 있거나 제일 큰게 들어오면
        MAX = H[i]
        stack = [H[i]]
        continue

    if stack[-1] <= H[i]: # 더 큰게 들어왔을때,
        while stack and stack[-1] <= H[i]: # 새로들어온게 더 크면 뽑는다,, 새로운게 작아지는 값이면 그만
            stack.pop()

        ans += len(stack)
        stack.append(H[i])
        continue

    if stack[-1] > H[i]: # 작은게 들어오면 편안하게 추가
        ans += len(stack)
        stack.append(H[i])
        continue

print(ans)