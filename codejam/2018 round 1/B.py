# 뒤집기
# Tag : ?
import sys
input = lambda: sys.stdin.readline().rstrip()

N, K, M = map(int, input().split())
# N ; nums of array
# K ; idx of array
# M ; nums of cal

array = [0] + list(map(int, input().split()))
def solve(start, end, k):
    if start > k or end < k:
        return k
    # start와 end어느쪽에 더 가까운지 확인 diff 찾기
    # 떨어진만큼 처리해서 k 값 return
    return start + end - k

for _ in range(M):
    command = int(input())
    if command < 0:
        K = solve(N + command + 1, N, K)
    else:
        K = solve(1, command, K)

print(K)
