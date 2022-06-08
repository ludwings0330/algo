import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

t = int(input())
while t:
    t -= 1
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    time = 0
    dq = deque()
    for i in range(1, n):
        if s[i] < f[i - 1]:
            s[i] = f[i - 1]
    d = [fi - si for fi, si in zip(f, s)]
    print(*d)