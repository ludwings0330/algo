# 1 <= n <= 10
# info.length = 11
# 맞힌 횟수가 같으면 어피치 점수 획득
# 최종 점수가 같을 경우 어피치 우승
def solution(n, info):
    answer = [0] * 11
    info_b = []

    for i in range(len(info)):
        if info[i] == 0:
            score_per_arrow = (10-i)
        else:
            score_per_arrow = (10-i)*2/(info[i]+1)
        # 화살당 점수, 갯수, 점수
        info_b.append([score_per_arrow, info[i]+1, 10-i])
    info_b = sorted(info_b, key=lambda x:(-x[0], x[2]))

    for score_per_arrow, m, score in info_b:
        if n - m >= 0:
            n -= m
            answer[10-score] = m
        else:
            answer[10-score] = 0
    if n > 0:
        answer[-1] += n
    check_score = 0
    for i in range(len(info)):
        if info[i] >= answer[i]:
            if info[i] == 0 and answer[i] == 0:
                continue
            check_score += (10-i)
        else:
            check_score -= (10-i)

    if check_score > 0:
        return [-1]
    else:
        return answer

    # 라이언이 가장 큰 점수 차이로 우승하기 위해 n 발의 화살을
    # 어떤 과녁 점수에 맞혀야하는지 10 점부터 0 점까지 순서대로 정수 배열에 담아 return


# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
print(solution(3, [3,3,3,3,3,3,3,2,0,0,0]))
