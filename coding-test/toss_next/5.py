## 작업은 한번에 2개 혹은 3개의 동일한 난이도 작업만 수행할 수 있다
from collections import Counter

def solution(tasks):
    answer = 0
    counter = Counter(tasks)
    for v in counter.values():
        quotient = v // 3
        remainder = v % 3
        if quotient == 0 and remainder == 1:
            return -1
        if remainder == 0:
            answer += quotient
        elif remainder == 2:
            answer += quotient + 1
        elif remainder == 1:
            quotient -= 1
            answer += quotient + 2
    return answer

print(solution([1,1,1,1,1,2,3]))