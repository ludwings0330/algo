import sys
input = lambda:sys.stdin.readline().rstrip()
import heapq

N = int(input())
process =[list(map(int, input().split()) + [i]) for i in range(N)]

# t, p, b, i
# 프로세스 실행 요청시점, 우선순위, 실행시간, 프로세스 번호

'''
우선순위 가장 높은 프로세스 실행
우선순위가 같으면 실행시간이 짧은 프로세스실행
우선순위와 실행시간이 같으면 프로세스 번호가 작은 프로세스부터 실행
'''

hq = []
process.sort(key = lambda x:x[0]) # 실행 요청 시점 순으로 정렬
idx = 0
while process[idx][0] <= process[0][0]:
    heapq.heappush(hq, process[idx])
    idx += 1


