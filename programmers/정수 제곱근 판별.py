## 제곱근 판별
def solution(n):
    answer = 0
    if int(n ** 0.5) == n**0.5:
        return int((n**0.5 + 1) ** 2)
    else:
        return -1

print(solution(121))
print(solution(3))

