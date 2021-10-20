# 미니 게임 k번 플레이, x 이상 x+k-1 이하의 정수 각각에 아래 미니 게임을 플레이
# x <= N <= x+k-1
# alice가 먼저시작하여 종이에 적힌 숫자보다 크지 않은 수 중 소수 P를 고른다
# 종이에 적힌 수가 X라면, 이를 지우고 X-P를 종이에 새로 적는다
# bob의 차례가 되어 이를 반복한다
# 만약 자신의 차례가 되었을때, 종이에 적힌수가 0 이나 1이라면 진다.
# X-P를 종이에 적을 때 이 값이 0 이나 1 이면 이긴다.
import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())

prime = [1] * (10**5 + 1)
prime[0] = prime[1] = 0

bob_win = [1] * (10**5 + 1)


for i in range(2, 10**5 + 1):
    if prime[i] == 1:
        k = 2
        while i * k <= 10**5:
            prime[i * k] = 0
            k += 1

for i in range(2, 10**5 + 1):
    if prime[i] == 1:
        bob_win[i] = 0
        bob_win[i+1] = 0



while TC:
    TC -= 1
    A, k = map(int, input().split())
    