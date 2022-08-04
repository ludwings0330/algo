import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
scores = list(map(int, input().split()))
a, b, k = map(int, input().split())

# 다음 인덱스로 넘어갈때 현재 각속도는 K 씩 감소
# 속도 v <= k 이면 장애물을 넘지 못한다.
# a, b 초기 각속도 최소, 최대
# 최소일때 어디서 멈추는지, 최대일때 어디서 멈추는지

v = a
a_idx = 0
while v > k:
    v -= k
    a_idx += 1
v = b
b_idx = 0
while v > k:
    v -= k
    b_idx += 1

ans = 0
if b_idx - a_idx >= N:
    ans = max(scores)
else:
    for i in range(a_idx, b_idx + 1):
        ans = max(ans, scores[i % N])

v = a
a_idx = 0
while v > k:
    v -= k
    a_idx -= 1
v = b
b_idx = 0
while v > k:
    v -= k
    b_idx -= 1

if abs(b_idx - a_idx) >= N:
    ans = max(ans, max(scores))
else:
    for i in range(a_idx, b_idx - 1, -1):
        ans = max(ans, scores[i%N])

print(ans)