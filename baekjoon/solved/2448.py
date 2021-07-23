import sys
from collections import deque
stars = ["  *   ",
         " * *  ",
         "***** "]

def star(s, e):
    if e-s == 3:
        for i in range(s, e):
            ans[i] += stars[i-s]
    else:
        for i in range(s, (s+e)//2):
            ans[i] += " "*((e-s)//2)
        star(s,(s+e)//2)
        for i in range(s, (s+e)//2):
            ans[i] += " "*((e-s)//2)
        star((s+e)//2, e)
        star((s+e)//2, e)
    pass

N = int(input())
ans = [""]*N
star(0,N)
for l in ans:
    print(l)