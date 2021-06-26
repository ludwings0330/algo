# 같은 학년은 같은 학년끼리 + 같은 성별은 같은 성별끼리 할때 필요한 방의 최소 갯수

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
gradeList = [[0, 0] for i in range(7)]
numOfRoom = 0
for i in range(N):
    S, Y = map(int, input().split())
    gradeList[Y][S] += 1

print(gradeList)
for grade in range(1, 7):
    girl, boy = gradeList[grade]
    while girl>0 or boy>0:
        if girl > 0:
            numOfRoom += 1
            girl -= K
        if boy > 0:
            numOfRoom += 1
            boy -= K

print(numOfRoom)