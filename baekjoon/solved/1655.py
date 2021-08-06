import sys
import heapq

input = sys.stdin.readline

N = int(input())
left, right = [],[]

while N:
    N -= 1
    n = int(input())

    if len(left) == len(right):
        # 왼쪽이 중앙값 보다 작은 수 들의 모임
        # 내림차순
        heapq.heappush(left, (-n, n))
    else:
        # 오른쪽이 중앙값보다 큰 수들의 모임
        # 오름차순
        heapq.heappush(right, (n, n))

    # 만약 오른쪽의 제일 작은 값 ( 중앙보다 큰수들 중에 제일 작은 값이)
    # 왼쪽의 제일 큰 값 보다 작으면 ( 중앙보다 작은 수들 중에 제일 큰 값)
    # 순서가 뒤바뀐 것이니까 두개를 바꿔준다. 중앙은 항상 중앙보다 작은 수들 중에 제일 큰 값이 정답이다.
    if right and right[0][1] < left[0][1]:
        nLeft = heapq.heappop(left)
        nRight = heapq.heappop(right)
        heapq.heappush(left, (-nRight[0], nRight[1]))
        heapq.heappush(right, (-nLeft[0], nLeft[1]))
    print(left[0][1])
