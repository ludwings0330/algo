'''
교과서 N권 방구석 M개 더미
교과서를 번호순으로 나열
N권 1 ~ N 까지 번호
맨 위의 교과서만 꺼낸다
'''

import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()

N, M = map(int, input().split())
books = []

for i in range(M):
    input()
    books.append(list(map(int, input().split())))

index = 1
hq = []

for i in range(M):
    heapq.heappush(hq, [books[i][-1], i, len(books[i])-1])

answer = True
while hq:
    current, m, n = heapq.heappop(hq)
    if index != current:
        answer = False
        break
    if n != 0:
        heapq.heappush(hq, [books[m][n-1], m, n-1])
    index += 1

if answer:
    print('Yes')
else:
    print('No')