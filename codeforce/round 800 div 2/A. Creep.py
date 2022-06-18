import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
while t:
    t -= 1
    zeros, ones = map(int, input().split())
    ans = ""
    for _ in range(min(zeros, ones)):
        print("10", end='')
    for _ in range(abs(zeros-ones)):
        print("0" if zeros > ones else "1", end='')
    print(ans)
