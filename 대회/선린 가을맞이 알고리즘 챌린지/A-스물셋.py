import sys
input = lambda:sys.stdin.readline().rstrip()


# 23으로만 이루어진 수의 합으로 나타낼 수 있는 모든 수중 k 번째로 작은 수출력

T = int(input())
while T:
    T -= 1
    k = int(input())
    print(23*k)