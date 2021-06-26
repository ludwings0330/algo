import sys
input = sys.stdin.readline

stack = [0]
N = int(input())
make = []
for _ in range(N):
    make.append(int(input()))

ans = []
f = 1
isAnswer = True
for n in make:
    if stack[-1] < n:
        while stack[-1] < n:
            stack.append(f)
            f += 1
            ans.append('+')
    ans.append('-')
    if stack.pop() != n:
        isAnswer ^= True
        break


if isAnswer:
    for ch in ans:
        print(ch)
else:
    print('NO')