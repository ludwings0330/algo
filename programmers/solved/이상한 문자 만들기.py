# 각 단어별 짝수번째는 대문자 홀수번째는 소문자
# 첫번째 인덱스는 0
def solution(s):
    answer = []
    index = 0
    for c in s:
        if c == ' ':
            index = 0
            answer.append(c)
        else:
            if index % 2 == 0:
                answer.append(c.upper())
            else:
                answer.append(c.lower())
            index += 1
    return ''.join(answer)


print(solution("try hello world"))
print(solution("aaaaaa aaaaa aaaaaa  "))
print(solution("aaaaaa   aaaaa    aaaaaa"))