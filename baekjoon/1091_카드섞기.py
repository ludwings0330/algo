import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

cards = [str(i) for i in range(N)]

# 카드를 한번섞으면 i 번째 위치에 있던 카드가 S[i] 번째 위치로 이동한다.
def mix():
    mixed_cards = [0] * N
    global cards
    for i in range(N):
        mixed_cards[S[i]] = cards[i]

    cards = mixed_cards


def isAnswer():
    for i in range(N):
        if i % 3 != P[int(cards[i])]:
            return False
    return True


loopChecker = set()

answer = -1
cnt = 0
while '-'.join(cards) not in loopChecker:
    loopChecker.add('-'.join(cards))
    if isAnswer():
        answer = cnt
        break
    cnt +=1
    mix()
print(answer)

