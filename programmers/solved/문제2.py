def solution(a):
    answer = 0
    minLeft = a[0]
    minRight = a[-1]
    DP = [0] * len(a)
    for i in range(1, len(a)):
        if a[i] < minLeft:
            minLeft = a[i]
        else:
            DP[i] += 1

    for i in range(len(a) - 2, 0, -1):
        if a[i] < minRight:
            minRight = a[i]
        else:
            DP[i] += 1

    for i in range(len(DP)):
        if DP[i] != 2:
            # print(a[i], end=' ')
            answer += 1

    # print(DP)
    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))