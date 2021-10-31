'''
황소 다마고치

1. 매일 낮, 황소에게 원하는 만큼 먹이를 줘 체력을 올린다.
    0 <= x <= 현재 가지고 있는 먹이의 개수
    -> 황소의 체력이 x 만큼 증가
2. 매일 밤, 황소의 체력이 절반으로 줄어든다(소수점이하는 버린다.). 체력이 0 이 되었다면 황소는 죽는다.

최대 며칠째까지 생존 가능할까??

소수점이 생기면 낭비가 되므로, 밤이 지나고 나서
---- 체력이 홀수면 1을 더하고 먹이의 개수를 1 줄인다. ----
체력과 먹이의 개수가 매우 많으니까. 빠르게 할 수 있는 방법은?
2씩 나누니까 빨리될거야. 체력이 1일때는 이제 남은 먹이 만큼 가능.

'''

import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())


def solve(n, m):
    if n == 1:
        return m + 1

    if n % 2 == 0:
        return solve(n//2, m) + 1

    elif n % 2 == 1:
        if m > 0:
            return solve((n+1)//2, m-1) + 1
        else:
            return solve(n//2, m) + 1

while T:
    T -= 1

    n, m = map(int, input().split())
    # 초기 체력 n, 먹이 갯수 m
    # 1 <= n, m <= 10 **12

    print(solve(n, m))
