import sys
input = sys.stdin.readline

s = input().rstrip()

oper = []
nums = []

for ch in s:
    if ch == '-' or ch == '+':
        oper.append(ch)


for s in s.split('+'):
    nums += list(map(int, s.split('-')))

sum = nums[0]
PLUS = True
for i in range(0, len(oper)):
    if oper[i] == '-':
        PLUS = False
    if PLUS:
        sum += nums[i+1]
    else:
        sum -= nums[i+1]

print(sum)