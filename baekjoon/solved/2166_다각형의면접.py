import sys
input = sys.stdin.readline
# N 각형 넓이 구하기 소수점 둘째에서 반올림
N = int(input())
pos = []

for i in range(N):
    x, y = map(int, input().split())
    pos.append([x, y])
pos.append(pos[0])

answer = 0
for i in range(N):
    answer = answer + pos[i][0] * pos[i+1][1] - pos[i][1] * pos[i+1][0]
if answer < 0:
    answer = -answer
area = answer * 0.5

print("%.1f" %area)

#
# import sys
# import math
# input = sys.stdin.readline
#
# n = int(input())
#
# coord_list = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     coord_list.append((x, y))
#
# coord_list.append(coord_list[0])		#(x1, y1) 좌표를 coord_list 마지막에 다시 추가
#
# plus = 0
# minus = 0
# for i in range(len(coord_list) - 1):
#     plus += (coord_list[i][0] * coord_list[i+1][1])
#     minus += (coord_list[i][1] * coord_list[i+1][0])
# area = math.fabs(0.5 * (plus - minus))
# print("%.1f" % area)