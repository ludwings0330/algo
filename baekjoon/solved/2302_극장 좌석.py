import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
VIPs = set([0] + [int(input()) for _ in range(M)] + [N+1])
VIPs = sorted(VIPs)
cache = [-1] * (N+1)
cache[0] = 1
cache[1] = 1
cache[2] = 2

for i in range(3, N+1):
    cache[i] = cache[i-1] + cache[i-2]

ans = 1
for i in range(1, len(VIPs)):
    ans *= cache[VIPs[i] - VIPs[i-1] - 1]
print(ans)
'''
VIP는 자기 자리에 앉아야한다.
VIP가 아닌 사람은 3가지 경우의 수가 있음
1. 자기자리 왼쪽
2. 자기자리
3. 자기자리 오른쪽

앉을 수 있는 경우의 수를 반환하세요.
1 <= N <= 40
0 <= M <= N  , 오름차순으로 입력
'''