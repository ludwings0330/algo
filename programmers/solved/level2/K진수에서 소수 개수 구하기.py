import math


def solution(n, k):
    decimal = []
    answer = 0
    while n:
        decimal.append(n % k)
        n //= k

    decimal = ''.join(map(str, decimal[::-1]))
    for num in [int(x) for x in decimal.split('0') if x != '']:
        isPrime = True if num > 1 else False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            answer += 1
    return answer

print(solution(1000000, 3))
print(solution(437674, 3))
print(solution(110011, 10))
print(solution(5, 10))
print(solution(1, 3))