'''
근우와 명우 카드게임

카드가 일렬로 있다,
왼쪽 카드 가져가기 vs 오른쪽 카드 가져가기

근우 먼저 시작,

둘다 최선을 다한다. 근우가 얻는 점수를 구하는 프로그램

어떻게 해야 최선일까?
좌우 중에 큰수를 가져간다? ㄴㄴ
좌우중에 큰걸 가져갔을 때, -> 그 밑에 있는 수가 엄청 크다면 최선이 아니다.


1 <= N <= 1000
'''
import sys
input = lambda:sys.stdin.readline().rstrip()

TC = int(input())

def game(left, right, player):
    if left == right:
        if player % 2 == 0:
            return cards[left]
        else:
            return 0

    if cache[player][left][right] != -1:
        return cache[player][left][right]


    if player % 2 == 0:
        cache[player][left][right] = max(game(left + 1, right, (player + 1) % 2) + cards[left],
                                         game(left, right - 1, (player + 1) % 2) + cards[right])
    else:
        cache[player][left][right] = min(game(left + 1, right, (player + 1) % 2),
                                         game(left, right - 1, (player + 1) % 2))
    # 오른쪽 뽑기

    return cache[player][left][right]


while TC:
    TC -= 1
    N = int(input())
    cards = list(map(int, input().split()))
    cache = [[[-1] * (N) for _ in range(N)] for _ in range(2)]

    print(game(0, N-1, 0))