# title : 오아시스 재결합
# tag : 스택

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stack = [(int(input()), 1)]

ans = 0
MAX = stack[0]
cnt = 1
for _ in range(N-1):
    h = int(input())

    while stack and stack[-1][0] < h:
        ans += stack.pop()[1]

    if not stack:
        stack.append((h, 1))
    else:
        if stack[-1][0] == h:
            cnt = stack.pop()[1]
            ans += cnt

            if stack:
                ans += 1

            stack.append((h, cnt+1))
        else:
            stack.append((h, 1))
            ans += 1

print(ans)