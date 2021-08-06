# 1 : 위 2 : 왼 3 : 아 4 : 오
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)

# 중앙 -> 다른곳 2
# 다른곳 -> 인접 3
# 다른곳 -> 반대 4
# 같은곳 -> 1
command = list(map(int, input().split()))

ans = 0
left = 0
right = 0
def move(a, b): # 발을 a 에서 b로 옮긴다.
    if a == b: # 같은 곳을 누를때 1
        return 1
    elif a == 0: # 중앙에서 움직일때 2
        return 2
    elif abs(b-a) == 2: # 반대쪽으로 갈때 4
        return 4
    else: # 나머지 3
        return 3

dp = set()

def solve(l, r, n):

    if n == len(command)-1:
        return 0

    ret = dp[l][r][n]
    if ret != 0:
        print('dp')
        return ret

    dp[l][r][n] = min(move(l, command[n]) + solve(command[n], r, n+1),
                      move(r, command[n]) + solve(l, command[n], n+1))
    print(l, r, n)
    return dp[l][r][n]
print(solve(0,0,0))
print()