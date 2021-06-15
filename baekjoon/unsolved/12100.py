# 2048 (EASY)
import sys
input = sys.stdin.readline

N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
    