# title ; GCD(n, k) = 1
# tag ; 최대 공약수

# GCD(n, k) =1 을 만족하는 K 1<=k<=n 의 개수를 구하는 프로그램 작성
# 1 <= n <= 10 ** 12

# 오일러 파이 함수
# pi(n) = x : n을 소인수 분해한게 n과 서로소인 것의 갯수 x

n = int(input())
ans = n

for i in range(2, round(n**0.5) + 1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        ans *= 1-(1/i)
if n > 1:
    ans *= 1-(1/n)
print(round(ans))