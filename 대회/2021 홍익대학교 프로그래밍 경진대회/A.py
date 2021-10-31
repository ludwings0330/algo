'''
응시 학생 수 N
A 비율 X%
A 학점을 받기위한 최소 점수 Y
상대 평가시 A 학점을 받는사람, 절대평가시 A  학점을 받는 사람
'''


N = int(input())
A = list(map(int, input().split()))
X, Y = map(int, input().split())

relative = 0
absolute = 0

relative = N * X/100
for i in range(N):
    if A[i] >= Y :
        absolute += 1

print(int(relative), absolute)