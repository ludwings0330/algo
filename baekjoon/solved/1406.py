import sys
input = sys.stdin.readline

S = list(input().rstrip())
M = int(input())

stack1 = S
stack2 = []

for _ in range(M):
    LEN = len(S)
    line = input().split()

    if line[0] == 'P': # 왼쪽에 line[1] 추가.
        stack1.append(line[1])

    elif line[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())

    elif line[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())

    elif line[0] == 'B': # 왼쪽 삭제
        if stack1:
            stack1.pop()

stack2.reverse()
print(''.join(stack1+stack2))