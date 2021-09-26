import sys
input = lambda: sys.stdin.readline().rstrip()


def recursive(arr, toPick):
    if toPick == 0:
        num = 0
        global dp
        for i in range(len(arr)):
            t = arr[i]
            num += dice[t//6][t%6] * (10**i)
            dp[num] = 1
        return

    for i in range(N*6):
        if not visit_dice[i//6]:
            visit_dice[i//6] = True
            recursive(arr + [i], toPick - 1)
            visit_dice[i//6] = False

def solution(dice):
    # 주사위 갯수 1 <= N <=4
    # 0 ~ 9 가 쓰여져 있다.
    answer = 1
    global N, visit_dice, dp
    N = len(dice)
    visit_dice = [False] * N
    dp = [0] * (10**5)

    recursive([], N)

    while True:
        if dp[answer] == 0:
            break

        answer += 1
    return answer


dice = [[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]
ans = solution(dice)
print(ans)

dice = [[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]
ans = solution(dice)
print(ans)