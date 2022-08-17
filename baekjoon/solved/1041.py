#     +---+
#     | D |
# +---+---+---+---+
# | E | A | B | F |
# +---+---+---+---+
#     | C |
#     +---+

# 2면 = (N-1) * 4 + (N-2) * 4 개
# 3면 = 4 개
# 1면 = (4*(N-2)*(N-1) + (N-2)**2)

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A, B, C, D, E, F = [0, 1, 2, 3, 4, 5]
dice = list(map(int, input().split()))

ans = 0
# 3개
MIN = float('inf')
for i, j, k in ((A, B, D), (A, B, C), (A, C, E), (A, E, D), (F, B, D), (F, B, C), (F, C, E), (F, E, D)):
    MIN = min(MIN, dice[i] + dice[j] + dice[k])
ans += MIN * 4

# 2개 더했을대 최소
MIN = float('inf')
for i in range(6):
    for j in range(i+1, 6):
        if (i, j) not in [(A, F), (F, A), (E, B), (B, E), (C, D), (D, C)]:
            MIN = min(MIN, dice[i] + dice[j])

ans += MIN * ((N-1) * 4 + (N-2) * 4)

# 1개
dice.sort()
ans += dice[0] * (4*(N-2)*(N-1) + (N-2)**2)

if N == 1:
    ans = sum(dice[:5])

print(ans)