# Title : 팰린드롬
# Tag : DP ?

import sys
input = lambda: sys.stdin.readline().rstrip()

word = input()
N = len(word)
dp = [[False] * N for _ in range(N)]