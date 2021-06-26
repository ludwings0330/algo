import math
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
a = [x2-x1, y2-y1]
b = [x4-x3, y4-y3]
ra = math.sqrt(a[0]**2 + a[1]**2)
rb = math.sqrt(b[0]**2 + b[1]**2)

if abs(a[0]*b[0] + a[1]*b[1]) == abs(ra*rb):
    print(0)
else:
