A, B = map(int, input().split())
# 1, 3 A
# 2, 1 A
# 3, 2 A
ans = 'B'
if (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):
    ans = 'A'

print(ans)
