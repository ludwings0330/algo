def solution(s):
    answer = -1

    for i in range(len(s)-2):
        tmp = int(s[i:i+3])
        if tmp // 100 == tmp % 10 == tmp %100 // 10:
            answer = max(answer, tmp)

    return answer