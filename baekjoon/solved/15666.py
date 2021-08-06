import sys
input = sys.stdin.readline
import copy

N, M = map(int, input().split())
nums = list(map(int, input().split()))
# 이미 출력했다는거를 저장해야해.
# 중복사용 X
# 사전순으로 증가하는 순서

ans = []
visit = [False] * N
overlap = {}
def solve(i, ret, topick):
    if topick == M:
        r = '/'.join([str(s) for s in ret])
        if r in overlap:
            return
        overlap[r] = True
        print(*ret)
        return

    for j in range(i, len(nums)):
        ret.append(nums[j])
        solve(j, ret, topick+1)
        ret.pop()
nums.sort()
solve(0, [], 0)