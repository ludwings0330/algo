import sys
sys.setrecursionlimit(10**9)
def solve(tree, w, t):
    if t == T:
        return 0

    if cache[tree][w][t] != -1:
        return cache[tree][w][t]

    cache[tree][w][t] = 0

    if trees[t] != tree:
        # 다른나무로 이동할까말까 선택필요
        if w > 0:
            # 움직일 수 있을 때 2가지 1.움직인다 2. 가만히 있는다.
            cache[tree][w][t] = max(solve(tree, w, t+1), solve(trees[t], w-1, t+1) + 1)
        else:
            cache[tree][w][t] = solve(tree, w, t+1)
            # 다른나무에서 떨어지는데 움직일수 없으면? 뭐 어떻게해 가만히있어야지
    else:
        # 같으면 1개먹은 거고 지금 나무그대로 다음으로 이동
        cache[tree][w][t] = solve(tree, w, t+1) + 1

    return cache[tree][w][t]
'''
다른 나무에서 자두가 떨어질때 두가지 방법이 있다.
1. 다른 나무로 재빨리 이동한다.
    1.1 하지만 움직일 수 있는 횟수가 남아있을 때만 움직일 수 있다. 먹은 갯수 + 1

2. 가만히 있는다.
    먹은 갯수 + 0

내가 있는 나무에서 자두가 떨어지면 가만히 받아먹고 시간이 증가한다. 먹은 갯수 + 1
'''

input = lambda: sys.stdin.readline().rstrip()

T, W = map(int, input().split())

trees = [int(input()) for _ in range(T)]
# i초에 trees[i] 나무에서 자두가 떨어진다.

cache = [[[-1] * (T+1) for _ in range(W+1)] for _ in range(3)]
# 받을 수 있는 최대 자두 개수

print(solve(1, W, 0))