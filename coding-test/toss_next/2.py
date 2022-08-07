import math
def solution(levels):
    answer = 0
    levels.sort()
    l = len(levels)

    start = math.ceil(l * 0.75)

    if start >= len(levels):
        return -1

    answer = levels[start:][0]

    return answer


print(solution([1,2]))