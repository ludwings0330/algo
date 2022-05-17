# 1 <= n <= 10
# info.length = 11
# 맞힌 횟수가 같으면 어피치 점수 획득
# 최종 점수가 같을 경우 어피치 우승
def solution(n, apeach_score):
    global answer, max_score
    answer = []
    max_score = 0

    def calc_score(lion_score):
        ret = 0
        for i in range(len(lion_score)):
            point = 10 - i
            if lion_score[i] == apeach_score[i] == 0:
                pass
            elif lion_score[i] > apeach_score[i]:
                ret += point
            elif lion_score[i] <= apeach_score[i]:
                ret -= point

        return ret


    def bruteforce(remain_arrows, index, score_sheet):
        if index == 11:
            if remain_arrows > 0:
                score_sheet[-1] += remain_arrows

            score = calc_score(score_sheet)
            global max_score, answer
            if score > max_score:
                max_score = score
                answer = score_sheet[:]
            elif score == max_score and score != 0:
                for i in range(10, -1, -1):
                    if answer[i] != score_sheet[i]:
                        answer = score_sheet[:] if score_sheet[i] > answer[i] else answer
                        break
            return

        arrows_to_win = apeach_score[index] + 1
        # 승리
        if remain_arrows >= arrows_to_win:
            bruteforce(remain_arrows - arrows_to_win, index + 1, score_sheet + [arrows_to_win])
        # 패배
        bruteforce(remain_arrows, index + 1, score_sheet + [0])

    bruteforce(n, 0, [])
    return answer if answer else [-1]

# 라이언이 가장 큰 점수 차이로 우승하기 위해 n 발의 화살을
    # 어떤 과녁 점수에 맞혀야하는지 10 점부터 0 점까지 순서대로 정수 배열에 담아 return


# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
print(solution(3, [0,0,1,0,0,0,0,0,0,1,0]))
print(solution(3, [1,0,0,0,0,0,0,1,1,1,0]))
