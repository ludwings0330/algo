# title : 가로등
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
TC = int(input())

while TC:
    TC -= 1
    N = int(input())
    # 2<= N <= 200,000
    # -10**9 <= x, y <= 10**9
    lamp = defaultdict(int)
    for _ in range(N):
        x, y = map(int, input().split())
        lamp[x] = y

    for i