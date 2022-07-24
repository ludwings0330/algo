import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
ROW = set()
COL = set()
table = defaultdict(lambda: defaultdict(int))
for i in range(N):
    q, s, v = map(int, input().split())
    # q : 품목 ID
    # s : 판매점 ID
    # v : 판매 수량

    ROW.add(s)
    COL.add(q)
    table[s][q] += v

ROW = sorted(list(ROW))
COL = sorted(list(COL))

for r in range(-1, len(ROW)):
    for c in range(-1, len(COL)):
        if r == c == -1:
            print('-1', end=' ')
            continue
        elif r == -1:
            print(COL[c], end=' ')
        elif c == -1:
            print(ROW[r], end=' ')
        else:
            print(table[ROW[r]][COL[c]], end=' ')
    print()