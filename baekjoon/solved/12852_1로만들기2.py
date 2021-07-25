# # X가 3으로 나누어떨어지면 3으로 나눈다
# # X가 2로 나누어 떨어지면 2로 나눈다
# # 둘다아니면 1을 뺀다
# from collections import deque
#
# N = int(input())
# visit = [0]*(N+1)
#
# dq = deque()
# dq.append([N, 0])
# visit[N] = str(N)+' '
#
# while dq:
#     n, c = dq.popleft()
#     if n == 1:
#         print(c)
#         print(visit[1].rstrip())
#         break
#
#     if  n%3 == 0 and not visit[n//3]:
#         dq.append([n//3, c+1])
#         visit[n//3] = visit[n] +str(n//3)+' '
#     if n%2 == 0 and not visit[n//2]:
#         dq.append([n//2, c+1])
#         visit[n//2] = visit[n] +str(n//2) +' '
#     if not visit[n-1]:
#         dq.append([n-1, c+1])
#         visit[n-1] = visit[n] +str(n-1) +' '
#
# # 세개 연산을 사용해서 1을 만들때, 연산을 사용하는 횟수의 최솟값.
from collections import deque

N = int(input())
visit = [[]]*(N+1)

dq = deque()
dq.append([N, 0])
visit[N] = [N]

while dq:
    n, c = dq.popleft()
    if n == 1:
        print(c)
        print(*visit[1])
        break

    if  n%3 == 0 and not visit[n//3]:
        dq.append([n//3, c+1])
        visit[n//3] = visit[n] + [n//3]
    if n%2 == 0 and not visit[n//2]:
        dq.append([n//2, c+1])
        visit[n//2] = visit[n] + [n//2]
    if not visit[n-1]:
        dq.append([n-1, c+1])
        visit[n-1] = visit[n] + [n-1]