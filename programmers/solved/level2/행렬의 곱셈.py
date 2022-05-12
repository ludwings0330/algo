def solution(arr1, arr2):
    if len(arr1[0]) != len(arr2):
        arr1, arr2 = arr2, arr1

    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for r in range(len(arr1)):
        for c in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[r][c] += arr1[r][k] * arr2[k][c]

    return answer
