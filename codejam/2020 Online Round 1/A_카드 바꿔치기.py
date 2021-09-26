# R , Y , B , 0 ~ 9
# Title : 조교 배치
# Tag : 해쉬

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
TC = int(input())

while TC:
    TC -= 1
    n = int(input())

    cards = defaultdict(int)

    before = input().split()
    for card in before:
        cards[card] += 1
    after = input().split()
    is_cheater = False
    for card in after:
        if cards[card] - 1 < 0:
            is_cheater = True
            break
        cards[card] -= 1

    print('CHEATER' if is_cheater else 'NOT CHEATER')