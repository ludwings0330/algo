#터렛
import sys
import math

input = sys.stdin.readline

T = int(input())
while T:
    T -= 1
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    R = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if R == 0:
        if r1 == r2:
            print(-1)
        elif r1 != r2:
            print(0)
    else:
        if R == r1 + r2:
            print(1)
        elif R > r1+ r2:
            print(0)
        elif r1+r2 > R:
            if max(r1, r2) > R: # 원이 내부에 있을때
                if max(r1, r2) == R + min(r1,r2):
                    print(1)
                elif min(r1, r2) + R < max(r1, r2):
                    print(0)
                else:
                    print(2)
            else:
                print(2)