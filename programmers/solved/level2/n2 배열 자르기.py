def solution(n, left, right):
    r = left // n
    c = left % n
    gap = right - left

    answer = []
    while left <= right:
        r = left // n
        c = left % n

        if r >= c:
            answer.append(r+1)
        else:
            answer.append(c+1)

        left += 1


    return answer

print(solution(3, 0, 9))
print(solution(4, 7, 14))