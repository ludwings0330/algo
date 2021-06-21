import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())
MAP = []
fish = []
sharkSize = 2

for _ in range(N):
    line = list(map(int, input().split()))
    for s in line:
        if s != 0:
            heapq.heappush(fish, s)
            fish += 1

for
