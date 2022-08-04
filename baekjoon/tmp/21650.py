import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
scores = list(map(int, input().split()))
rank = sorted(scores, reverse = True)

shot_winner = False
candidate = set()
for i in range(N - 1):
    if not shot_winner and scores[i] == rank[0]:
        shot_winner = True
        continue
    if shot_winner:
        if scores[i] % 10 == 5 and scores[i+1] < scores[i]:
            candidate.add(scores[i])

store = set()
if len(candidate) == 0:
    print(0)
else:
    count = 1
    for score in rank:
        if score in candidate:
            print(count)
            break
        count += 1
        store.add(score)