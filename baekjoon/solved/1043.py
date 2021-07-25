import sys
input = sys.stdin.readline

N, M = map(int , input().split())
truth = set()
truth.update(list(map(int, input().split()))[1:])
parties = [set() for _ in range(M)]
for _ in range(M):
    parties[_].update(list(map(int, input().split()))[1:])

ans = 0
for i in range(M+1):
    for j in range(M):
        if i == M:
            if not (truth & parties[j]):
                ans+=1
            continue
        if truth & parties[j]:
            truth.update(parties[j])

print(ans)