# title : 신비로운 수
# N개의정수를 M으로 나눈 나머지가 모두 같다

# 신비로운 수 M 중에서 가장 큰 수를 구해보자
import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())
while TC:
    TC -= 1
    N = int(input())
    array = list(map(int, input().split()))

    