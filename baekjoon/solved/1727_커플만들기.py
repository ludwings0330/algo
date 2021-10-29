'''
2 1
10 20
15

5

couple(m, w) 남자 번호 m 부터, 여자번호 w 부터 커플을 짝지었을 때 성격차이의 최소합 반환

'''
import sys
input = lambda: sys.stdin.readline().rstrip()

INF = 987654321

def couple(w, m):
    if w == W:
        return 0
    if m == M:
        return 0

    if cache[w][m] != -1:
        return cache[w][m]

    cache[w][m] = INF
    for nm in range(m, M-(W-w-1)):
        cache[w][m] = min(cache[w][m], couple(w+1, nm+1) + abs(man[nm] - woman[w]))

    return cache[w][m]



M, W = map(int, input().split())
man = list(map(int, input().split()))
woman = list(map(int, input().split()))

man.sort()
woman.sort()

if len(man) < len(woman):
    man, woman = woman, man
    M, W = W, M

cache= [[-1] * M for _ in range(W)]

print(couple(0, 0))