import sys
input = sys.stdin.readline
stack = []
N = int(input())
for i in range(N):
    c = int(input())
    if c == 0 and stack :
        stack.pop()
        continue
    stack.append(c)
print(sum(stack))