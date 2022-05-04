def solution(x, n):
    answer = []
    num = x
    while n > 0:
        n -= 1
        answer.append(num)
        num = num + x
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))