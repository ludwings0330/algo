import sys
input = lambda: sys.stdin.readline()

t = int(input())
while t:
    t -= 1

    n, k = map(int, input().split())
    s = list(input().rstrip())

    ones = s.count('1')
    add = 0

    left = right = 0

    for i in range(len(s)):
        if s[i] == '1':
            left = i
            break
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            right = i
            break

    if ones and k >= len(s) - 1 - right:
        ones -= 1
        add += 1
        k -= len(s) - 1 - right

    if ones and k >= left:
        ones -= 1
        add += 10
        k -= left

    print(11*ones + add)
