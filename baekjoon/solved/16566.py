# 문제 제목 : 카드게임
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
Min = list(map(int, input().split()))
Fe = list(map(int, input().split()))

Min.sort()
use = set()
def upper_bound(target, arr):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left+right)//2
        if arr[mid] <= target:
            left = mid +1
        else:
            right = mid

    return right
c = [False]*(N+1)
for card in Fe:
    index = upper_bound(card, Min)
    while index <= N and c[index]:
        index += 1
    print(Min[index])
    c[index] = True