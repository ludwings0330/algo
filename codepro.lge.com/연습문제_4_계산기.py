import sys
input = sys.stdin.readline().rstrip()

TC = int(input())

while TC:
    TC -= 1
    type, numA, numB = map(int, input().split())
    ans = ''
    # numA * numB 를 32진법으로 출력