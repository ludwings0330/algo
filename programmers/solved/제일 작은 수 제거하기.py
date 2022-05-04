def solution(arr):
    answer = []

    min_value = min(arr)

    for num in arr:
        if num != min_value:
            answer.append(num)

    if len(answer) == 0:
        return [-1]

    return answer


print(solution([10]))
print(solution([4, 3, 2, 1]))