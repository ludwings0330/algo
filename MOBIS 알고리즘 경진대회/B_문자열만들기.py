def solution(a):
    answer = []

    for ss in a:
        left, right = 0, len(ss)
        cnt_a = ss.count('a')
        cnt_b = ss.count('b')
        isTrue = True
        while left < right:
            if ss[left] == 'a':
                left += 1
                cnt_a -= 1

                continue
            if ss[right - 1] == 'a':
                right -= 1
                cnt_a -= 1

                continue

            if ss[left] == ss[right - 1] == 'b':
                tleft, tright = left, right
                cnt = 0
                while tleft < tright and cnt != cnt_a:
                    if ss[tleft] == ss[tright -1] == 'b':
                        cnt_b -= 2
                        cnt += 1
                        tleft += 1
                        tright -= 1
                        continue
                    else:
                        break
                if cnt != cnt_a or cnt_a == 0:
                    isTrue = False
                    break
                else:
                    left = tleft
                    right = tright

        answer.append(isTrue)
    return answer

a = ["abab","bbaa","bababa","bbbabababbbaa"]
print(solution(a))