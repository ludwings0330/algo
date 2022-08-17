import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
posts = [list(map(int, input().split())) for _ in range(n)]

stack = []

for k, post in enumerate(posts):
    if not stack:
        stack.append(post+[k])
        continue
    for i in range(len(stack)-1, -1, -1):
        if post[0] <= stack[i][0] <= stack[i][1] <= post[1]:
            stack.pop(i)
        elif stack[i][0] <= post[0] <= post[1] <= stack[i][1]:
            l, r, tk = stack.pop(i)
            stack.append([l, post[0]-1, tk])
            stack.append([r, post[1] + 1, tk])
        elif stack[i][0] <= post[0] <= stack[i][1]:
            stack[i][1] = post[0] - 1
        elif stack[i][0] <= post[1] <= stack[i][1]:
            stack[i][0] = post[1] + 1

    stack.append(post+[k])

print(len(set(post[2] for post in stack)))
