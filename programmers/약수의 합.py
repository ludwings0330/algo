# n의 모든 약수의 합


def solution(n):
    answer = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            answer.add(i)
            answer.add(n//i)
    return sum(answer)

print(solution(12))
print(solution(5))
