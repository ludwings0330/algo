import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N, K = map(int, input().split())
store = defaultdict(int)

for _ in range(N):
    # 여학생 0, 남학생 1
    S, Y = map(int, input().split())
    key = str(S) + str(Y)
    store[key] += 1

answer = 0
for num in store.values():
    answer += num//K
    if num%K != 0:
        answer += 1
print(answer)