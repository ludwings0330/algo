'''
24 * N 시간 이후 시험 시작
기말고사 M개
1 부터 M
최저점 0 점 최고점 100점

최소 ai 한시간 공부할때 bi 점
최고점을 넘을 수 없다. 찬우가 받을 수 있는 최종 성적의 최대 값.
'''

import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N, M = map(int, input().split())
# M개 과목, N일후 시험시작
a = list(map(int, input().split()))
# 각 과목 최소점수
b = list(map(int, input().split()))
# 각 과목 1시간 공부시 오르는 점수

# m번 과목에 ki 시간을 투자한다.
'''
m번 과목에 ki 시간을 투자한다. 최대점을 받위해서 효율이 높은 거부터 해야지
b 내림차순 정렬
'''

myArr = list(zip(a, b))

myArr.sort(key = lambda x: (x[1]), reverse=True)
hq = []
for i in range(len(myArr)):
    heapq.heappush(hq, [-myArr[i][1], 100 - myArr[i][0]])
    # 1시간 공부시 오르는 점수, 올릴 수 있는 점수

time = N * 24
# N * 24 시간 있음
score = sum(a)
while hq:
    b, a = heapq.heappop(hq)
    b *= -1
    if a//b <= time:
        score += (a//b) * b
        time -= (a//b)
        a %= b
    else:
        score += time*b
        break

    if a < b:
        b = a

    if a != 0:
        heapq.heappush(hq, [-b, a])
print(score)