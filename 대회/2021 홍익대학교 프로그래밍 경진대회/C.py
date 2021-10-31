'''
C번 - 초콜릿 뺏어 먹기

N개의 통에 초콜릿 -> 오름차순이 되도록 배열

1. K < i 인  i 를 볼라, i- K 번째 통에 있는 초콜릿의 개수가 똑가탕질때까지 i번ㅉ ㅒ통에서 초콜릿 꺼내먹음
2. 통을 재정렬, -> 오름차순이 되도록

연두가 눈치채지 못하는 선에서 ㅚ대ㅠ한 많이, 그리고 최대한 빨리

최대한 많이, 최대한 빨리... 몇개나 먹을 수 있을까??

최대한 빨리 최대한 많이
1. 최대한 빨리 -> 가장 많이 먹을 수 있는 통을 선택한다.
2.
'''



import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

a = list(map(int, input().split()))

MIN = min(a)
ans = 0
cnt = 0
for i in range(N):
    ans += a[i] - MIN
    if a[i] != MIN:
        cnt += 1

print(ans, cnt)