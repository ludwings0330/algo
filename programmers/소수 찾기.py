# 1~n  까지에 있는 숫자중 소수의 갯수 반

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if prime[i]:
            answer += 1
    return answer


prime = [True] * 1000001
for i in range(2, 1000001):
    if prime[i]:
        k = 2
        while i * k < 1000001:
            prime[i * k] = False
            k += 1

print(solution(10))
print(solution(5))