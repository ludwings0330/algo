import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

# +, -, *, /
# 식의 결과가 최소인 걸 ㄱㄱ

MAX = -sys.maxsize
MIN = sys.maxsize

def solve(a, i):
    if i == N:
        global MAX, MIN
        MAX = max(MAX, a)
        MIN = min(MIN, a)
        return
    for j in range(4):
        if operators[j] > 0:
            operators[j] -= 1
            if j == 0:
                solve(a+nums[i], i+1)
            elif j == 1:
                solve(a-nums[i], i+1)
            elif j == 2:
                solve(a*nums[i], i+1)
            else:
                solve(int(a/nums[i]), i +1)
            operators[j] += 1
solve(nums[0], 1)
print(MAX)
print(MIN)
