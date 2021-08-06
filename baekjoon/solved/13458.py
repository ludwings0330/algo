#시험감독
import sys

input = sys.stdin.readline

# i번 시험장 응시자 수 Ai 명
# 총감독관 1명 : B 명 감시
# 부 감독관 여러명 : C 명 감시
# 감독관 수의 최솟값

N = int(input())
# 1 <= N <= 1000000
A = list(map(int,input().rstrip().split()))
# A 각 시험장에 있는 응시자의 수
B, C = map(int, input().split())
# B : 총 감독관이 확인할 수 있는수, C : 부 감독관이 볼 수 있는 수.
answer = 0

for n in A:
    answer += 1
    n -= B
    if n <= 0:
        continue
    a = n//C
    answer += a+1 if n%C != 0 else a
print(answer)